# Design Documents Standard

## Convention

Every feature or architectural decision should be documented as a standalone Markdown file inside the `docs/design_docs/` folder. Each design doc includes YAML frontmatter (`created`, `status`) and follows the template below. Files are named using sequential numbering (`NNNN-kebab-case-title.md`) and the index below is kept up to date grouped by status.

## Benefits

- AI agents and developers get self-contained, discoverable references requiring no extra context.
- Sequential numbering provides stable references even as documents change status.
- Status metadata makes it easy to filter proposed vs. implemented vs. rejected docs.
- The index enables quick scanning of all design docs in one place.
- Version controlled alongside source code without external tooling.

## Examples

### Good: Filled-in design doc following the template

````markdown
---
created: 2026-03-05
status: Implemented
---

# Criteria Sorting Support

## Overview

Add sorting support to the criteria pattern so callers can specify sort fields and direction.

## Objectives

- Allow sorting by any field on the target entity
- Support ascending and descending order
- Keep the criteria pattern unchanged for consumers

## Requirements

### Functional Requirements

- Accept a list of `SortField` objects with `field` and `direction`
- Default to ascending if direction is not specified
- Apply sorts in the order they are provided

### Non-Functional Requirements

- Zero performance overhead when no sorting is used

## Usage Examples

```python
criteria = EmployeeCriteria(
    sorts=[SortField("last_name", ASC), SortField("first_name", ASC)]
)
employees = repository.find(criteria)
```

## Implementation Steps

1. Add `SortField` value object with `field` and `direction` properties
2. Add `sorts` property to base `Criteria` class
3. Update repository implementations to apply sorts when building queries

## Open Questions

- Should we support nested field sorting (e.g. `department.name`)?
````

### Template

Copy this template when creating a new design doc:

````markdown
---
created: YYYY-MM-DD
status: Proposed
---

# Feature Title

## Overview

Brief description of the feature (1-2 sentences). What problem does it solve?

## Objectives

- Objective 1
- Objective 2
- Objective 3

## Requirements

### Functional Requirements

- Requirement 1
- Requirement 2
- Requirement 3

### Non-Functional Requirements

- Performance requirement
- Security requirement
- Scalability requirement

## Usage Examples

### Example 1: Basic Usage

```python
# Code example showing how the feature will be used
```

### Example 2: Advanced Usage

```python
# Code example showing advanced use case
```

## Implementation Steps

Use vertical slicing: each step should deliver a small end-to-end increment of value, not a horizontal layer (e.g., "add UI" → "add API" → "add database"). A good vertical step is one that could theoretically be demoed or merged on its own.

1. Step 1 - Description
2. Step 2 - Description
3. Step 3 - Description
4. Step 4 - Description

## Open Questions

- Question 1?
- Question 2?
- Question 3?

## Notes

Additional context, considerations, or references.
````

### Bad: Missing metadata or structure

```markdown
# Feature Title

Some scattered notes about what this feature should do.
No status, no date, no structured sections.
```

## Real world examples


## Related agreements

- [ADR Guidelines](../adrs/adr-guidelines.md) — documents the same documentation standard applied to ADRs

## Design Documents

### Implemented

| Number | Title | Created | Link |
|--------|-------|---------|------|
| -      | -     | -       | -    |

### Proposed

| Number | Title | Created | Link |
|--------|-------|---------|------|
| 0001   | MetricsMiddleware Refactor | 2026-06-03 | [link](0001-metrics-middleware-refactor.md) |

### In Progress

| Number | Title | Created | Link |
|--------|-------|---------|------|
| -      | -     | -       | -    |

### On Hold

| Number | Title | Created | Link |
|--------|-------|---------|------|
| -      | -     | -       | -    |

### Rejected

| Number | Title | Created | Link |
|--------|-------|---------|------|
| -      | -     | -       | -    |