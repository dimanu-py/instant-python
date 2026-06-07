---
name: convention
description: Create or improve convention documentation based on the current conversation. Use this when a feature's learnings should be captured as reusable conventions.
---

Create new or improve existing documentation files inside the `docs/conventions` folder.

## Steps

1. Identify conventions, patterns, or decisions discussed or discovered during the feature that should be documented.
2. Check if a relevant doc already exists in `docs/conventions` (organized by area: `architecture/`, `testing/`, `workflow/`).
   - If it exists, improve it while preserving the required structure.
   - If it does not exist, create a new file in the appropriate subfolder.
3. Read `docs/conventions/convention-guidelines.md` and follow its structure exactly. Every document MUST include these sections in order:
```
# Name of the convention

## Convention
## Benefits
## Examples (with Good and Bad subsections)
## Real world examples
## Related agreements
```
4. Ask the human to confirm the target file path before writing.
5. Record the new convention path so consuming agents can discover it.

## Rules

- Each convention goes in its own standalone Markdown file — never bundle multiple conventions into one doc.
- Place files in the correct area subfolder (`architecture/`, `testing/`, `workflow/`).
- Include concrete good and bad examples with code blocks when applicable.
- Link to real files in the codebase that follow the convention in the "Real world examples" section.
