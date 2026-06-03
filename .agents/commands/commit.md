---
name: commit
description: Split uncommitted changes into atomic conventional commits with a focus on why each change was made. Use only when the user explicitly invokes this command.
---

Split the currently uncommitted changes into multiple atomic conventional commits. This command is **conversational**: you will ask the user before every decision.

## Steps

1. Run `git status` and `git diff` (staged + unstaged) to see everything that exists. For files with multiple unrelated hunks, also inspect `git diff` per file.

2. Propose a grouping plan: list each commit you would create, which files (or hunks) go into it, and the conventional commit subject you suggest. Show this as a numbered list. Each commit must represent a **chunk of correct functional code** — it should compile and work on its own.

3. **Ask the user** to confirm or correct the grouping before doing anything.

4. For each commit in the agreed order:
   - Stage exactly the files (or hunks via `git add -p` if needed) that belong to this commit. Never use `git add .` or `git add -A`.
   - Draft a subject line and **optional body** that explain **why** the change was made, not just what changed. Ask yourself: does the commit benefit from extra context? If yes, include a body. If the subject already tells the full story, omit the body.
   - Confirm the subject and body (if any) with the user.
   - Commit with the subject line only, or subject + body if applicable.
   - Run `git status` to confirm only the intended files were committed.

5. After the last commit, run `git status` and `git log --oneline` so the user can verify the result.

## Commit message guidance

- The subject should express **intent**: *what was done and why* (e.g., `feat(api): add rate limiting to prevent abuse` rather than `feat(api): add rate limiting`).
- Add a body only when the subject alone doesn't capture the reasoning. The body is for context: trade-offs considered, alternatives rejected, or non-obvious implications.
- Use `!` after the type/scope to mark a breaking change (e.g., `feat(api)!: remove deprecated v1 endpoints`). If breaking, also include a `BREAKING CHANGE:` trailer in the body explaining the migration path.
- Reference issues with `Closes #123`, `Fixes #456`, or `Refs #789` in the body when applicable.
- If in doubt about whether a body adds value, ask the user.

## Commit types

| Type       | When to use                                                                                                                                                    |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `feat`     | Code changes that add new functionality, modify existing behavior/return values (often breaks tests), or remove a feature.                                     |
| `fix`      | Changes that fix a bug — either an unidentified bug, or a test that broke after a behavior change and needs correction.                                        |
| `refactor` | Changes that modify existing code without altering its behavior: type hints, removing unused imports, renaming variables, etc.                                 |
| `test`     | Changes related only to tests: object mothers, fixing a test that was incorrectly implemented, renaming test variables, reorganizing test structure.           |
| `style`    | Formatting changes that don't modify code behavior (whitespace, formatting, etc.).                                                                             |
| `build`    | Changes to the build process, dependencies, or tooling that don't affect code behavior.                                                                        |
| `docs`     | Documentation changes like README, ADRs, or design docs.                                                                                                       |
| `chore`    | Changes that don't fit other types and don't touch src, tests, or docs (e.g., .gitignore, editor config).                                                      |
| `ci`       | Changes to CI/CD pipeline files or configuration.                                                                                                              |
| `perf`     | Performance improvements that change behaviour to make it faster.                                                                                              |

## Questions you should ask

- Is this grouping correct, or should X go with Y instead?
- For the proposed subject `feat(api): add rate limiting to prevent abuse`, is the scope right?
- Does this commit deserve a body, or is the subject enough?
- Should any change be discarded instead of committed?

Err on the side of asking more rather than less.

## Hard rules

- **No Claude attribution.** Never add `Co-Authored-By: Claude`, `🤖 Generated with Claude Code`, or any similar footer.
- **No `--no-verify`.** If a hook fails, stop and ask the user.
- **Never bundle unrelated changes.** If two changes share a file but belong in different commits, use `git add -p` to split them.
- **Do not push.**
