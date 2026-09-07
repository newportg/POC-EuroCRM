<#
.SYNOPSIS
    Phase 0 provisioning: Azure SQL (Bicep) + Dataverse environment (Power Platform).

.DESCRIPTION
    Deploys the SQL system of record via main.bicep, then creates the Dataverse
    environment with the Power Platform admin PowerShell module (Dataverse
    environments are not ARM/Bicep-deployable).

    After this script, three short manual steps complete Phase 0:
      1. make.powerapps.com -> Solutions -> add "Virtual Connector Provider" from AppSource
      2. Make a SQL Server connection (Connections) using sqlServerFqdn / database / login
      3. Run sql/spike-schema.sql against EuroCRMPOC (SSMS / Azure Data Studio / sqlcmd)
      Then run the relationship spike: Entity Catalog -> create virtual tables,
      confirm N:1 lookups + filtered views, record go/no-go in POC.md.

.PARAMETER ResourceGroup
    Azure resource group name (created if missing). Default rg-eurocrm-poc.

.PARAMETER Location
    Azure region. Default westeurope (EU data residency per the wiki).

.PARAMETER EnvironmentName
    Name prefix for SQL resources. Default eurpoc.

.PARAMETER SqlAdminPassword
    SQL admin password (mandatory). POC only - Key Vault for prod.

.PARAMETER LoginUsername
    Account used to sign in to Azure CLI and Power Platform.
    Default gary.newport@devknightfrank.onmicrosoft.com. MFA-enabled: authentication is
    interactive (browser / device code) and must be completed TWICE - once for Azure CLI,
    once for Power Platform.

.PARAMETER DataverseDisplayName
    Dataverse environment display name. Default "EuroCRM POC".

.PARAMETER DataverseLocation
    Power Platform location. Default europe (EU data residency).

.PARAMETER DataverseSku
    Trial | Developer | Sandbox | Production. Default Developer (free, POC).

.EXAMPLE
    .\deploy.ps1 -SqlAdminPassword 'P@ssw0rd!X'
.NOTES
    Prerequisites: Azure CLI (az), and the Microsoft.PowerApps.Administration.PowerShell module
    (Install-Module Microsoft.PowerApps.Administration.PowerShell -Scope CurrentUser).
#>
[CmdletBinding()]
param(
    [string]$SubscriptionId,
    [string]$ResourceGroup = 'rg-eurocrm-poc',
    [string]$Location = 'westeurope',
    [string]$EnvironmentName = 'eurpoc',
    [string]$DatabaseName = 'EuroCRMPOC',
    [string]$SqlAdminLogin = 'sqladmin',
    [Parameter(Mandatory = $true)]
    [string]$SqlAdminPassword,
    [string]$LoginUsername = 'gary.newport@devknightfrank.onmicrosoft.com',
    [string]$DataverseDisplayName = 'EuroCRM POC',
    [string]$DataverseLocation = 'europe',
    [ValidateSet('Trial', 'Developer', 'Sandbox', 'Production')]
    [string]$DataverseSku = 'Developer'
)

$ErrorActionPreference = 'Stop'
$scriptDir = $PSScriptRoot

Write-Host '== EuroCRM POC - Phase 0 provisioning ==' -ForegroundColor Cyan

# 1. Azure CLI sign-in -----------------------------------------------------
# Target account: $LoginUsername (MFA-enabled — authentication is interactive).
az account show *> $null
if ($LASTEXITCODE -ne 0) {
    Write-Host "Signing in as $LoginUsername - complete the sign-in in the browser (MFA required)."
    az login --username $LoginUsername
    if ($LASTEXITCODE -ne 0) {
        Write-Host 'Username-prompt login failed (expected for some MFA setups). Signing in interactively - choose the account in the browser.'
        az login --use-device-code
    }
    if ($LASTEXITCODE -ne 0) { throw 'az login failed.' }
}

# Verify the signed-in account is the intended one (MFA accounts are easy to mix up).
$currentUser = (az account show --query "user.name" -o tsv)
if ($currentUser -and $currentUser -ne $LoginUsername) {
    throw "Signed in as $currentUser, expected $LoginUsername. Run 'az login --use-device-code' manually, pick the right account, then re-run this script."
}
Write-Host "Azure CLI signed in as: $currentUser"

if ($SubscriptionId) {
    az account set --subscription $SubscriptionId
    if ($LASTEXITCODE -ne 0) { throw "Failed to set subscription $SubscriptionId" }
}

# 2. Resource group ---------------------------------------------------------
az group create --name $ResourceGroup --location $Location *> $null
if ($LASTEXITCODE -ne 0) { throw "Failed to create resource group $ResourceGroup" }
Write-Host "Resource group ready: $ResourceGroup ($Location)"

# 3. Deploy Bicep (SQL server + database + firewall) -------------------------
Write-Host 'Deploying Bicep template (SQL)...'
$deployName = "phase0-$((Get-Date -Format 'yyyyMMddHHmmss'))"
$deployJson = az deployment group create `
    --resource-group $ResourceGroup `
    --template-file "$scriptDir\main.bicep" `
    --parameters environmentName=$EnvironmentName databaseName=$DatabaseName `
        sqlAdminLogin=$SqlAdminLogin sqlAdminPassword=$SqlAdminPassword `
    --name $deployName | ConvertFrom-Json

$outputs = $deployJson.properties.outputs
if (-not $outputs) { throw 'Bicep deployment did not return outputs.' }
Write-Host "SQL server : $($outputs.sqlServerName.value)" -ForegroundColor Green
Write-Host "SQL FQDN   : $($outputs.sqlServerFqdn.value)" -ForegroundColor Green
Write-Host "Database   : $($outputs.sqlDatabaseName.value)" -ForegroundColor Green

# 4. Dataverse environment (Power Platform) ---------------------------------
Write-Host 'Creating Dataverse environment via Power Platform admin...'
Import-Module Microsoft.PowerApps.Administration.PowerShell -ErrorAction Stop

# Connect with an existing session if possible, otherwise sign in.
if (-not (Get-Command Get-AdminPowerAppEnvironment -ErrorAction SilentlyContinue)) {
    throw 'Power Platform admin module not installed. Run: Install-Module Microsoft.PowerApps.Administration.PowerShell -Scope CurrentUser'
}
Write-Host "Signing in to Power Platform as $LoginUsername - complete the prompt (MFA required)."
Connect-PowerAppsAccount -Username $LoginUsername

$env = Get-AdminPowerAppEnvironment | Where-Object { $_.DisplayName -eq $DataverseDisplayName }
if ($env) {
    Write-Host "Dataverse environment already exists: $($env.EnvironmentName)" -ForegroundColor Yellow
}
else {
    $env = New-AdminPowerAppEnvironment `
        -DisplayName $DataverseDisplayName `
        -Location $DataverseLocation `
        -EnvironmentSku $DataverseSku `
        -DatabaseLanguage 1033 `
        -DatabaseCurrency 'EUR'
    Write-Host "Dataverse environment created: $($env.EnvironmentName)" -ForegroundColor Green
}

# 5. Manual next steps -------------------------------------------------------
Write-Host ''
Write-Host '== Phase 0 remaining steps (manual) ==' -ForegroundColor Cyan
Write-Host ' 1. make.powerapps.com -> Solutions -> install "Virtual Connector Provider" from AppSource'
Write-Host " 2. Data -> Connections -> create SQL Server connection:"
Write-Host "      Server: $($outputs.sqlServerFqdn.value)  Database: $DatabaseName  Login: $SqlAdminLogin"
Write-Host " 3. Run POC\infra\sql\spike-schema.sql against the database (SSMS / sqlcmd)"
Write-Host ' 4. Entity Catalog -> create virtual tables; test Account -> Contact -> Deal -> DealProperty chain'
Write-Host ' 5. Record the go/no-go decision in POC.md'