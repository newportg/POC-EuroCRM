// EuroCRM POC — Phase 0 infrastructure
// Provisioning the SQL system of record for the virtual-table architecture.
// The Dataverse environment itself cannot be deployed via ARM/Bicep — deploy.ps1
// creates it afterwards with the Power Platform admin PowerShell module.

targetScope = 'resourceGroup'

@description('Azure region for the POC resources. Defaults to the resource group location.')
param location string = resourceGroup().location

@description('Short prefix used in resource names, e.g. eurpoc -> eurpoc-sql.')
param environmentName string = 'eurpoc'

@description('SQL server administrator login.')
param sqlAdminLogin string = 'sqladmin'

@secure()
@description('SQL server administrator password. POC only — move to Key Vault for anything longer-lived.')
param sqlAdminPassword string

@description('SQL database name (system of record).')
param databaseName string = 'EuroCRMPOC'

@description('SKU — General Purpose Serverless (pausable, low cost for POC).')
param databaseSku string = 'GP_S_Gen5'

@description('vCores for the serverless database.')
@minValue(1)
@maxValue(80)
param databaseCapacity int = 1

@description('Minutes of inactivity before the serverless database auto-pauses. 60 = pause after 1 hour.')
param autoPauseDelay int = 60

@description('Optional client firewall rules, e.g. [ { name, startIpAddress, endIpAddress } ]. Empty by default.')
param clientIpRules array = []

@description('Entra ID principal login to set as SQL Entra admin (user or group). Empty to skip.')
param sqlEntraAdminLogin string = ''

@description('Entra ID object ID of the principal above. Empty to skip.')
param sqlEntraAdminObjectId string = ''

var sqlServerName = '${environmentName}-sql'

// --- SQL server -----------------------------------------------------------

resource sqlServer 'Microsoft.Sql/servers@2022-05-01-preview' = {
  name: sqlServerName
  location: location
  properties: {
    administratorLogin: sqlAdminLogin
    administratorLoginPassword: sqlAdminPassword
    minimalTlsVersion: '1.2'
    publicNetworkAccess: 'Enabled'
  }
}

// Required so Azure services (incl. the Dataverse Virtual Connector Provider) can reach the DB.
resource allowAzureServices 'Microsoft.Sql/servers/firewallRules@2022-05-01-preview' = {
  parent: sqlServer
  name: 'AllowAllWindowsAzureIps'
  properties: {
    startIpAddress: '0.0.0.0'
    endIpAddress: '0.0.0.0'
  }
}

// Optional explicit client ranges (e.g. your workstation) for direct SSMS access.
resource clientRules 'Microsoft.Sql/servers/firewallRules@2022-05-01-preview' = [for (rule, i) in clientIpRules: {
  parent: sqlServer
  name: 'ClientRule_${i}_${rule.name}'
  properties: {
    startIpAddress: rule.startIpAddress
    endIpAddress: rule.endIpAddress
  }
}]

// Entra ID administrator (preferred over SQL auth for the connector).
resource sqlEntraAdmin 'Microsoft.Sql/servers/administrators@2022-05-01-preview' = if (sqlEntraAdminObjectId != '') {
  parent: sqlServer
  name: 'ActiveDirectory'
  properties: {
    administratorType: 'ActiveDirectory'
    login: sqlEntraAdminLogin
    sid: sqlEntraAdminObjectId
    tenantId: subscription().tenantId
  }
}

// --- SQL database ---------------------------------------------------------

resource sqlDatabase 'Microsoft.Sql/servers/databases@2022-05-01-preview' = {
  parent: sqlServer
  name: databaseName
  location: location
  sku: {
    name: databaseSku
    tier: 'GeneralPurpose'
    family: 'Gen5'
    capacity: databaseCapacity
  }
  properties: {
    collation: 'SQL_Latin1_General_CP1_CI_AS'
    maxSizeBytes: 34359738368 // 32 GB — plenty for the POC
    minCapacity: 0.5
    autoPauseDelay: autoPauseDelay
  }
}

// --- Outputs --------------------------------------------------------------

output sqlServerName string = sqlServer.name
output sqlServerFqdn string = sqlServer.properties.fullyQualifiedDomainName
output sqlDatabaseName string = sqlDatabase.name
output sqlAdminLogin string = sqlAdminLogin
@description('Connection string template — replace CHANGE_ME with the admin password.')
output sqlConnectionString string = 'Server=tcp:${sqlServer.properties.fullyQualifiedDomainName},1433;Initial Catalog=${databaseName};Persist Security Info=False;User ID=${sqlAdminLogin};Password=CHANGE_ME;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;'