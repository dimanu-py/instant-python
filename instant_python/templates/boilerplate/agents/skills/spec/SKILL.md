---
name: spec
description: Create or update .spec files in docs/features/ using the established format. Use when a feature needs to be documented before Gherkin scenarios are written.
---

# Spec

Creates or updates `.spec` files inside `docs/features/`. A `.spec` captures a feature's purpose, behavior, contract, edge cases, and decisions before any code is written.

## Format

Every `.spec` document MUST include these sections in order:

```markdown
# Feature Name

## Purpose

One sentence describing what the feature does.

## Behavior

Precise prose describing what the feature does: inputs, processing, and outputs. No implementation details.

## Contract

- **Inputs**: request shape (path params, query params, body schema)
- **Outputs**: response shape (status codes, body schema)

## Edge Cases

Enumerated list of edge cases and how the system handles each:
- Case one: description
- Case two: description

## Decisions

Each decision with its rationale and the discarded alternative.
- **Decision**: what was chosen
- **Rationale**: why
- **Alternative**: what was rejected and why

## Open Questions

Unresolved items (mark as resolved or remove when decided).
```

## Rules

- One `.spec` per feature, named `docs/features/<name>.spec`
- Every claim must be convertible to a Given/When/Then scenario. If not testable, refine it or mark as open.
- Every decision must record the alternative that was rejected and why.
- Do not include implementation details or code.
