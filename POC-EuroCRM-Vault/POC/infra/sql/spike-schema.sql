-- EuroCRM POC — Phase 0 spike schema
-- Minimal tables to validate the virtual-table relationship chain:
-- kf_account -> kf_contact -> kf_deal -> kf_dealproperty
--
-- Follows the Phase 0 schema rules:
--   * GUID primary keys (uniqueidentifier DEFAULT NEWID())
--   * int / nvarchar only — no bigint, datetime2, geometry, geography, rowversion
--   * FK columns exactly match the referenced PK (ExternalName discipline)
--
-- Full Phase B/C schema (all 24 tables, stage machine, temporal audit) comes later.

IF (DB_NAME() != 'EuroCRMPOC')
    PRINT N'Warning: not connected to EuroCRMPOC — verify before running.';

GO

-- Client ---------------------------------------------------------------
CREATE TABLE dbo.kf_account (
    kf_accountid            uniqueidentifier NOT NULL CONSTRAINT DF_kf_account_id DEFAULT NEWID(),
    kf_name                 nvarchar(160)    NOT NULL,
    kf_accounttype          int              NOT NULL,        -- 0 Investor, 1 Vendor, 2 Occupier
    kf_accountclassification int             NULL,            -- 0 Brand/Group, 1 Legal Entity, 2 Individual
    kf_entitytype           int              NULL,            -- 0 Fund, 1 SPV, 2 JV ...
    kf_registrationnumber   nvarchar(50)     NULL,            -- SIREN / HRB / KRS
    kf_industry             int              NULL,            -- mapped to kf_siccode later
    kf_country              nvarchar(2)      NULL,            -- FR / DE / ES / PL
    kf_emailaddress1        nvarchar(100)    NULL,
    kf_telephone1           nvarchar(50)     NULL,
    kf_parentaccountid      uniqueidentifier NULL,
    CONSTRAINT PK_kf_account PRIMARY KEY (kf_accountid),
    CONSTRAINT FK_kf_account_parent FOREIGN KEY (kf_parentaccountid) REFERENCES dbo.kf_account (kf_accountid)
);

CREATE TABLE dbo.kf_contact (
    kf_contactid            uniqueidentifier NOT NULL CONSTRAINT DF_kf_contact_id DEFAULT NEWID(),
    kf_firstname            nvarchar(100)    NOT NULL,
    kf_lastname             nvarchar(100)    NOT NULL,
    kf_jobtitle             nvarchar(100)    NULL,
    kf_emailaddress1        nvarchar(100)    NULL,
    kf_telephone1           nvarchar(50)     NULL,
    kf_accountid            uniqueidentifier NULL,            -- FK, matches kf_account.kf_accountid (ExternalName)
    kf_processingconsent    int              NULL,            -- 0 Not assessed, 1 Legitimate interest, 2 Consent, 3 Legal obligation
    CONSTRAINT PK_kf_contact PRIMARY KEY (kf_contactid),
    CONSTRAINT FK_kf_contact_account FOREIGN KEY (kf_accountid) REFERENCES dbo.kf_account (kf_accountid)
);

-- Property --------------------------------------------------------------
CREATE TABLE dbo.kf_property (
    kf_propertyid           uniqueidentifier NOT NULL CONSTRAINT DF_kf_property_id DEFAULT NEWID(),
    kf_name                 nvarchar(200)    NOT NULL,        -- primary-name field
    kf_sector               int              NULL,
    kf_propertytype         int              NULL,
    kf_status               int              NULL,
    kf_tenure               int              NULL,
    kf_addressfull          nvarchar(400)    NULL,
    kf_country              nvarchar(2)      NULL,
    CONSTRAINT PK_kf_property PRIMARY KEY (kf_propertyid)
);

-- Deal ------------------------------------------------------------------
CREATE TABLE dbo.kf_deal (
    kf_dealid               uniqueidentifier NOT NULL CONSTRAINT DF_kf_deal_id DEFAULT NEWID(),
    kf_name                 nvarchar(200)    NOT NULL,        -- primary-name field
    kf_stage                int              NOT NULL DEFAULT 1,  -- S1..S8 = 1..8
    kf_dealstatus           int              NULL,            -- 0 Active, 1 Won, 2 Lost
    kf_accountid            uniqueidentifier NULL,            -- client org (Brand/Group)
    kf_contactid            uniqueidentifier NULL,            -- primary deal contact
    kf_legalentityaccountid uniqueidentifier NULL,            -- contractual counterparty
    kf_country              nvarchar(2)      NULL,
    CONSTRAINT PK_kf_deal PRIMARY KEY (kf_dealid),
    CONSTRAINT FK_kf_deal_account FOREIGN KEY (kf_accountid) REFERENCES dbo.kf_account (kf_accountid),
    CONSTRAINT FK_kf_deal_contact FOREIGN KEY (kf_contactid) REFERENCES dbo.kf_contact (kf_contactid),
    CONSTRAINT FK_kf_deal_legalentity FOREIGN KEY (kf_legalentityaccountid) REFERENCES dbo.kf_account (kf_accountid)
);

-- Junction: one deal, many properties -------------------------------------
CREATE TABLE dbo.kf_dealproperty (
    kf_dealpropertyid       uniqueidentifier NOT NULL CONSTRAINT DF_kf_dealproperty_id DEFAULT NEWID(),
    kf_name                 nvarchar(200)    NOT NULL,        -- primary-name field
    kf_dealid               uniqueidentifier NOT NULL,
    kf_propertyid           uniqueidentifier NOT NULL,
    kf_allocationpercent    decimal(9,2)     NULL,
    kf_passingrent          decimal(18,2)    NULL,
    kf_erv                  decimal(18,2)    NULL,
    CONSTRAINT PK_kf_dealproperty PRIMARY KEY (kf_dealpropertyid),
    CONSTRAINT FK_kf_dealproperty_deal FOREIGN KEY (kf_dealid) REFERENCES dbo.kf_deal (kf_dealid),
    CONSTRAINT FK_kf_dealproperty_property FOREIGN KEY (kf_propertyid) REFERENCES dbo.kf_property (kf_propertyid)
);

-- Indexes for the spike ----------------------------------------------------
CREATE INDEX IX_kf_contact_account ON dbo.kf_contact (kf_accountid);
CREATE INDEX IX_kf_deal_account ON dbo.kf_deal (kf_accountid);
CREATE INDEX IX_kf_dealproperty_deal ON dbo.kf_dealproperty (kf_dealid);
CREATE INDEX IX_kf_dealproperty_property ON dbo.kf_dealproperty (kf_propertyid);

-- Seed two rows so the chain can be walked immediately ---------------------
INSERT dbo.kf_account (kf_name, kf_accounttype, kf_accountclassification, kf_country)
VALUES (N'Blackstone Group', 0, 0, N'FR'),
       (N'Blackstone Core Fund', 0, 1, N'FR');
INSERT dbo.kf_contact (kf_firstname, kf_lastname, kf_accountid)
SELECT N'Ada', N'Lovelace', kf_accountid FROM dbo.kf_account WHERE kf_name = N'Blackstone Core Fund';
INSERT dbo.kf_property (kf_name, kf_country)
VALUES (N'Tour La Défense', N'FR');
INSERT dbo.kf_deal (kf_name, kf_stage, kf_accountid)
SELECT N'FR Office Portfolio', 1, kf_accountid FROM dbo.kf_account WHERE kf_name = N'Blackstone Group';
INSERT dbo.kf_dealproperty (kf_name, kf_dealid, kf_propertyid)
SELECT N'Lot 1', kf_dealid, (SELECT kf_propertyid FROM dbo.kf_property WHERE kf_name = N'Tour La Défense') FROM dbo.kf_deal WHERE kf_name = N'FR Office Portfolio';

-- Verification: run this to confirm the chain ------------------------------
-- SELECT a.kf_name AS account, c.kf_firstname AS contact,
--        d.kf_name AS deal, dp.kf_name AS lot, p.kf_name AS property
-- FROM dbo.kf_account a
-- LEFT JOIN dbo.kf_contact c ON c.kf_accountid = a.kf_accountid
-- LEFT JOIN dbo.kf_deal d ON d.kf_accountid = a.kf_accountid
-- LEFT JOIN dbo.kf_dealproperty dp ON dp.kf_dealid = d.kf_dealid
-- LEFT JOIN dbo.kf_property p ON p.kf_propertyid = dp.kf_propertyid;