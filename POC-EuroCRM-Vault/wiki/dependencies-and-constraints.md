---
status: Draft
parent:"[[solution-overview]]"
---

# Dependencies and Constraints

## Key Dependencies

| Dependency                      | Type       | Impact    | Status     |
| ------------------------------- | ---------- | --------- | ---------- |
| TDA Approval                    | Governance | Must have | Pending    |
| CTO Architecture Principles     | Document   | Must have | Referenced |
| Regional legal review           | Compliance | Must have | Pending    |
| Enterprise integration platform | Technical | Must have | TBD        |
| ECS (Enterprise Connectivity Services) | Technical | Must have | TBD        |

**Note:** Major entity create/update events must be published to the Knight Frank ECS platform — the internal notification and message bus that notifies other systems of changes. ECS access, topic contracts, and payload schemas are an integration dependency to be confirmed with the enterprise integration team.
| Vendor selection                | Decision   | Must have | Pending    |

## Constraints

- TDA governance oversight required
- Regional data residency requirements
- Existing system integrations
- Budget and resource limitations (TBD)
