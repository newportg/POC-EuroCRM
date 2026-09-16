---
parent:"[[solution-overview]]"
status: Draft
author: Gary Newport
date: 15/09/2026
tags:
  - executive
  - architecture
  - decisions
  - tda
  - board
---

## European CRM Architectural Options - One-Page Summary

> Full version: [[architecture-approach-executive-summary]]

| Version | 0.01 Draft |
| --- | --- |
| Date | 15 September 2026 |
| Author | Gary Newport |

# Document History

| Version | Date | Author | Notes |
| --- | --- | --- | --- |
| 0.01 Draft | 15 Sept 26 | Gary Newport | Initial version for comment. |

# Terms used in this paper

| Term | Meaning in this paper |
| --- | --- |
| **Packaged capability** | A function that Microsoft supplies and maintains as part of Dynamics 365 Sales. |
| **Domain extension** | A Knight Frank table, relationship, process or rule that is added to the selected application. |
| **Model-driven application** | A Power Apps application that uses Dataverse tables, forms and views. |
| **Knight Frank-built application** | An application that Knight Frank designs, builds and operates. |
| **Enterprise integration** | A managed API or messaging service with monitoring, recovery and clear ownership. |
| **Total cost of ownership** | Implementation and operating costs across a period that shows the material cost differences between the options. |

# Executive summary

Knight Frank is proposing a shared European system for clients, contacts, properties, instructions and engagements. The proposed data model contains Knight Frank terms, classifications and business relationships. After reviewing the proposed entity design, each potential solution will need to enable support for the model(s).

The need for a custom data model should not require Knight Frank to build a new CRM platform.

Dynamics 365 Sales is built on the foundations of Microsoft Dataverse and is designed to support domain specific extensions (custom models). This capability enables Knight Frank to adopt the SaaS capabilities of Dynamics 365 Sales while extending the underlying data model to accommodate property, instruction and engagement data specific to the proposal.

The Board is asked to compare three application options:

- Extend Dynamics 365 Sales
- Build a separate model driven application on Dataverse
- Build a Knight Frank application.

The comparison should include all implementation and operating costs. It must also identify the CRM capabilities that Knight Frank would build and maintain under each option.

**Recommended position.**

Fund a defined validation stage.

Use Option A, extending Dynamics 365 Sales, as the baseline. Compare it with Option B, a separate model-driven application on Dataverse.

Retain Option C, a Knight Frank-built application, only where strategic, scale, performance or integration requirements justify full product ownership (unlikely in the case).

**What the validation stage will produce**

- An assessment of the fit with Dynamics 365 Sales.
- A total cost of ownership model.
- An assessment of integration requirements.
- A validation test of one representative end to end scenario.
- A recommendation for the application option and its operating model.

# Comparison of the application options

| Decision factor | Extend Dynamics 365 Sales | Model driven application on Dataverse | Knight Frank built application |
| --- | --- | --- | --- |
| **Application** | Use Dynamics 365 Sales as the main CRM application. Add Knight Frank domain extensions. | Build a separate CRM application with Power Apps and Dataverse. | Build and operate a custom CRM application and data platform. |
| **Packaged capability** | Retain standard relationship, activity, security and Microsoft 365 capabilities when they meet the requirements. | Retain Dataverse platform services. Knight Frank owns the CRM application above them. | Build or integrate all required CRM and Microsoft 365 capabilities. |
| **Specialist model** | Add custom tables beside standard account, contact and activity tables. | Add the same custom tables to a separate Knight Frank application. | Define and implement the complete data model and related services. |
| **Build and change** | Configure and extend the product. Do not recreate packaged capabilities that meet the requirements. | Build forms, navigation, processes and automation. Own testing, releases and support. | Own the full software lifecycle. This option requires the most engineering work. |
| **Cost basis** | Include Dynamics licences, Dataverse capacity, automation, implementation, support and change. | Include Power Apps licences, Dataverse capacity, automation, implementation, support and change. | Include cloud and software costs and the continuing cost of product, engineering, security, testing and operations. |
| **Integration** | Use enterprise integration for critical system exchanges. Use Power Automate for workflows with limited scope. | Use the same integration rule. Do not use distributed flows as the integration backbone. | Design enterprise APIs and messaging. Build the required Microsoft 365 integrations. |
| **Main risk** | Knight Frank could pay for packaged functions that users do not use. Excessive customisation could make product updates difficult. | Knight Frank could recreate Dynamics capabilities and understate the cost to maintain them. | Knight Frank could understate the continuing product cost and the time needed to provide mature CRM capabilities. |
| **Role in validation** | Use as the baseline for the fit and cost assessment. | Use as the main comparator. | Use only if strategic or technical requirements justify full ownership. |

# Option A: Extend Dynamics 365 Sales

## Proposition

Use Dynamics 365 Sales as the CRM and relationship management application. Add Knight Frank tables for property, instruction, deal, bid, NDA (Non-Disclosure Agreement), KYC (Know Your Customer), due diligence and reference data.

## Pros

- Microsoft supplies and supports the standard Dynamics 365 Sales application, entities and packaged CRM capabilities. Knight Frank remains responsible for its configuration, extensions, integrations and service operation.

- Knight Frank can use standard account, contact, lead and activity capabilities where they meet the requirements. The delivery team can concentrate on the property and advisory capabilities that are genuinely distinctive.

- Knight Frank avoids building and maintaining CRM application behaviour that Microsoft already provides. This can reduce delivery effort, testing effort and the amount of application functionality that Knight Frank must support.

- Dynamics 365 Sales provides product-specific Copilot capabilities for sales records. Microsoft documents capabilities for record summaries, recent changes and meeting preparation. Availability depends on the applicable licences and configuration.

- Microsoft develops the Sales agent across Dynamics 365 Sales, Outlook, Teams and other Microsoft 365 applications. This gives Knight Frank a supported route to future improvements, while retaining custom domain entities for its specialist data.

## Cons

- The licence cost can exceed the value if users make little use of the packaged capabilities.

- Knight Frank must still configure and govern the domain model, forms, processes, security and integrations.

- Knight Frank must test, release and support all Knight Frank extensions.

- Microsoft controls the product roadmap and release schedule. Knight Frank must assess changes and maintain compatibility with its extensions.

## Risks

- A superficial assessment could overstate the amount of packaged capability that Knight Frank can reuse.

- Custom logic could depend on internal Dynamics 365 Sales processes. This dependency could make product updates more difficult.

- Incorrect assumptions about users, environments or data growth could understate cost.

## When to use

Use this option when standard relationship, activity, productivity and security capabilities meet a material part of the requirement. Add the distinctive value through Knight Frank domain extensions.

## Justification

The option already uses standard Dynamics 365 entities account, contact, lead, business unit, user and activity concepts. The validation must measure the packaged capability that Knight Frank can retain. We should not reject Dynamics 365 Sales only because some advisory tables are custom.

# Option B: Build a model-driven application on Dataverse

## Proposition

Build a separate Knight Frank CRM application with Power Apps and Dataverse. Do not use the packaged Dynamics 365 Sales application.

## Pros

- Knight Frank can design the application around its own terminology, navigation and advisory processes.

- Knight Frank can implement its specialist property, instruction, deal and taxonomy model without adapting the user experience to the packaged sales process.

- Knight Frank avoids Dynamics 365 Sales licences where the validation shows that the packaged application provides insufficient value.

- Knight Frank retains the security, audit, data management and application services that Dataverse provides.

- A model-driven application can reduce development effort compared with a fully custom application. Knight Frank can configure tables, forms, views and processes on a common platform.

## Cons

- Knight Frank owns the CRM application above Dataverse. This includes its navigation, forms, views, processes and application behavior.

- Knight Frank must design, test, release, support and improve the application. Low-code tools reduce some development effort, but they do not remove these responsibilities.

- Knight Frank does not automatically receive all packaged Dynamics 365 Sales capabilities. The program must replicate & build, configure, integrate each required capability.

- The option retains Dataverse capacity, platform governance, automation licensing and specialist support dependencies. It does not reduce the commercial comparison to a simple difference in user license price.

- Complex custom tables and relationships can require more design, optimisation and testing. Large forms, extensive related data and distributed business logic can also make the application harder to change and support.

## Risks

- The program could recreate/duplicate functions & capabilities that Dynamics 365 Sales already supplies. This could increase delivery cost and continuing maintenance.

- Large data volumes, complex relationships, inefficient queries or synchronous automation could cause unacceptable response times. The validation stage must test representative data volumes, user journeys and concurrent activity.

- Integrations or bulk processes could exceed Dataverse request or service protection limits. Microsoft states that unusually demanding applications can receive throttling responses and that client applications must manage retries.

- Logic could become distributed across flows, plug-ins, business rules and application configuration. This can make behaviour difficult to trace, test and support.

- The cost model could leave out product ownership, regression testing, releases, support and continuing change. This would understate the total cost of the option.

## When to use

Use this option when the detailed assessment shows that Dynamics 365 Sales gives insufficient value. Knight Frank must also accept responsibility for the CRM product on Power Platform.

## Justification

This option transfers the application layer to Knight Frank. Low-code can reduce some development effort. It does not remove product ownership, testing, release management or support.

# Option C: Build a Knight Frank application

## Proposition

Build a custom CRM product and data platform with the enterprise engineering stack.

## Pros

- Knight Frank has full control over the user experience, domain behaviour, data architecture and release strategy.

- Knight Frank can design the application around its property and advisory services without adapting them to a packaged CRM product.

- Measured functional and non-functional requirements can determine the architecture, technology and data storage patterns.

- Knight Frank can optimise high volume, complex or time-sensitive processes where a packaged product or Dataverse cannot meet validated requirements.

- Knight Frank can control the pace and priority of product changes. It does not need to align its application roadmap with changes to a packaged CRM product.

## Cons

- Knight Frank must fund and operate the complete application lifecycle. This includes product management, architecture, engineering, testing, security, deployment, monitoring, support and continual improvement.

- Knight Frank must build, integrate or omit the CRM capabilities that packaged products supply. These can include account and contact management, activities, relationship management, workflows, audit and security.

- Knight Frank must design and maintain all required integrations with Outlook, Microsoft Teams, SharePoint and other Microsoft 365 services.

- The option requires the largest engineering and operational capability. Knight Frank must retain the necessary skills for as long as the application remains in use.

- Knight Frank is responsible for application performance, availability, recovery, accessibility and security. These responsibilities cannot be transferred to a CRM product provider.

## Risks

- The investment case could present the option as an infrastructure build and omit continuing product, engineering, testing, security and support costs.

- The program could focus on the specialist property and client model while underestimating the standard CRM capabilities that users expect.

- Delivery could take longer than planned because the team must create both the specialist functions and the supporting application services.

- Long-term ownership could depend on a small group of engineers or suppliers. Staff changes could then affect support, security and the rate of future development.

- Bespoke integrations with Microsoft 365 and other enterprise services could require continuing maintenance as interfaces, security controls and dependent services change.

## When to use

Use this option only when strategic, scale, performance or integration requirements justify full product ownership.

## Justification

The specialist property and client model does not, by itself, justify a Knight Frank built CRM application. The Board needs evidence that product constraints or economics outweigh the continuing cost and risk of full ownership.

# Evidence that the validation stage will produce

| Evidence | Expected result |
| --- | --- |
| **Fit with Dynamics 365 Sales** | Map each requirement to reuse, configuration, extension or custom behaviour. |
| **Total cost of ownership** | Cover implementation and a sufficiently long operating period. Include licences, Dataverse capacity, automation, environments, testing, support, releases, change and decommissioning. |
| **Integration requirements** | Define volume, latency, availability, retries, recovery, replay, monitoring, security, reconciliation and ownership. |
| **Application ownership and support** | Identify the product owner, platform and engineering responsibilities, support model, release frequency and regression approach. |
| **Representative solution test** | Test one end-to-end scenario across client, property, instruction, workflow, security, reporting and one critical system exchange. |

# Recommended Board position

Approve funding for a defined architecture validation stage.

This approval will fund the work that is necessary for an investment ready recommendation. It does not commit Knight Frank to full implementation of an application option.

Use Option A as the baseline. Use Option B as the main comparator.

Retain Option C when strategic or technical requirements justify full ownership (unlikely in this case).

Require a total cost of ownership model that uses Knight Frank enterprise licence terms and realistic assumptions.

Require an integration design that separates user workflow from critical system exchange.

Return to the Investment Board with the preferred option, quantified costs, residual risks and accountable owners.
