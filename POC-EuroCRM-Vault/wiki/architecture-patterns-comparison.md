---
parent:"[[solution-overview]]"
status: Draft
author: Gary Newport
date: 09/09/2026
tags:
  - architecture
  - integration
  - ecs
  - golden-source
---

# Architecture Patterns — Integration to Golden Source

Three integration patterns for populating a Golden Source database from a CRM system. Each shows a different mechanism for getting entity data from the system of engagement into the authoritative master data store consumed by BI, Finance, and downstream systems.

## Pattern 1 — Dynamics 365 Direct Export

The simplest pattern. Dynamics 365 / Dataverse is the primary CRM system. Entity data is exported on a scheduled basis (or manually) to the Golden Source database.

- Export runs as a batch job — full or incremental sync
- Mapping and transform layer handles schema differences between Dataverse and the target store
- No real-time sync — data freshness depends on export frequency
- Suitable when downstream consumers can tolerate near-daily staleness

![[dynamics-export-to-golden-source.png]]

## Pattern 2 — Dynamics 365 + ECS Message Bus

Dynamics 365 remains the system of engagement, but entity changes are captured in near-real-time via the ECS (Enterprise Connectivity Services) message bus.

- Dataverse change tracking or a Power Automate flow captures entity mutations
- Changes are published as events to an ECS topic
- A consumer worker service subscribes, transforms, and upserts into the Golden Source
- Decouples the CRM from downstream consumers — multiple systems can subscribe to the same change stream
- Near-real-time freshness; failed messages route to a dead-letter queue for retry

![[dynamics-ecs-messagebus-to-golden-source.png]]

## Pattern 3 — C# / ASP.NET Core + ECS Message Bus

No Dynamics or Dataverse dependency. A custom ASP.NET Core application writes directly to PostgreSQL as the primary data store, and publishes entity changes to the ECS bus via the Outbox Pattern.

- Application commits write the domain event and outbox record in the same database transaction
- A background dispatcher publishes outbox events to ECS — guarantees exactly-once delivery
- External consumers (Finance bridge, BI feeds, other lines of business) subscribe to the ECS topic
- Golden Source database is the application's own PostgreSQL — no separate copy/sync step
- Full control over schema, security model, and change capture without platform constraints

![[csharp-stack-ecs-to-golden-source.png]]

## Comparison

| Aspect | Pattern 1 — Direct Export | Pattern 2 — Dynamics + ECS | Pattern 3 — C# + ECS |
| ------ | ------------------------- | -------------------------- | ---------------------- |
| CRM system | Dynamics 365 / Dataverse | Dynamics 365 / Dataverse | Custom ASP.NET Core |
| Sync mechanism | Scheduled batch export | Event-driven via ECS bus | Outbox pattern → ECS bus |
| Data freshness | Near-daily | Near-real-time | Near-real-time |
| Platform dependency | High (Dataverse) | High (Dataverse) | None (first-party code) |
| Downstream decoupling | Low — tight coupling to export schema | High — multiple ECS subscribers | High — multiple ECS subscribers |
| Operational complexity | Low | Medium — requires ECS infrastructure | Medium — requires ECS infrastructure |
| Licensing | Per-user / per-org Dataverse | Per-user / per-org Dataverse | Infrastructure cost only |

## Related

- [[csharp-postgresql/alternative-architecture-traditional-csharp]] — Full Option C design using C# and PostgreSQL
- [[solution-overview]] — Parent document
- [[power-platform-dataverse/architecture-application]] — Option B application and integration patterns
