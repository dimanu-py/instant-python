---
name: design-doc
description: Create or improve design documents based on the current conversation. Use this when a new feature or architectural
  change has been discussed that should be captured as a design doc.
---

Based on the current conversation or an existing plan, create new or improve existing design documents inside the `docs/design_docs` folder.

## Steps

1. Identify features, architectural decisions, or requirements discussed in the conversation that should be captured as a design doc.

2. Check if a relevant design doc already exists in `docs/design_docs`.
    - If it exists, improve it while preserving the required structure.
    - If it does not exist, determine the next sequential number by looking at existing filenames (format `NNNN-kebab-case-title.md`).

3. Read `docs/design_docs/design-doc-guidelines.md` and follow its structure exactly. Every document MUST include:
   - YAML frontmatter with `created` (YYYY-MM-DD) and `status` (Proposed, In Progress, Implemented, On Hold, Rejected)
   - These sections in order:
   ```
   # Feature Title

   ## Overview
   ## Objectives
   ## Requirements (with Functional and Non-Functional subsections)
   ## Usage Examples
   ## Implementation Steps (use vertical slicing — each step is an end-to-end increment)
   ## Open Questions
   ## Notes (optional)
   ```

4. Ask the user to confirm the target file path before writing.

5. Add the new entry to the appropriate status table in `docs/design_docs/design-doc-guidelines.md`.

## Rules

- Each feature or architectural decision goes in its own standalone design doc — never bundle multiple features into one doc.
- Use the next available sequential number (e.g., 0005 if 0004 is the highest).
- Implementation steps MUST use vertical slicing: each step delivers a small end-to-end increment of value, not a horizontal layer (e.g., avoid "add domain classes" → "add infrastructure" → "add tests").
- Include concrete usage examples with code blocks when applicable.
- Set the status to "Proposed" for new docs, and update it as the feature progresses through the lifecycle.
