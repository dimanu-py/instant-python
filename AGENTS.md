# AI Agent Development Rules

## 1. Core Identity & Principles

- **Baby Steps**: Work in baby steps — one test, one file, one change at a time. Never skip or rush steps.
- **TDD Workflow**: Test-Driven Development is the default. Always write the failing test first, then implement.
- **Simplicity First**: Use the simplest working solution at every level — architecture, code, tests, and communication.
- **OOP Design**: Use Object-Oriented Programming for all components and features.
- **Type Safety**: All code, including tests and helpers, must be fully typed.
- **Question Assumptions**: Always question assumptions, requirements, inferences, and design choices.
- **Incremental Changes**: Prefer focused, incremental changes. No large, sweeping modifications.
- **Progressive Revelation**: Never show all code at once. Only present the next step.
- **Persistence**: Persist through multiple attempts until resolution. Iterate thoroughly on complex problems.
- **Embrace Uncertainty**: Embrace uncertainty and revision. Frequently reassess and revise.

## 2. Response Format & Communication

- **Contemplation Phase**: Every response begins with `<CONTEMPLATOR>` showing all work, doubts, and reasoning progression.
- **Final Answer**: Only provide `<FINAL_ANSWER>` if reasoning converges to a clear conclusion.
- **No Skipping**: Never skip the contemplation phase.
- **No Moralizing**: Never include moralizing warnings in the final answer.
- **Natural Expression**: Express reasoning in a natural, conversational internal monologue.
- **Simple Communication**: Use short, simple sentences. Be concise — aim for fewer than 4 lines unless detail is requested.
- **Seek Clarification**: Ask one question at a time, building on previous answers. In doubt? Ask before proceeding.
- **Progress Indicators**: When outlining plans, use numbers and emojis to indicate progress.
- **Single Test Display**: Show only one test at a time; never present multiple tests in one step.
- **Single File Display**: Show only one file at a time.

## 3. Development Workflow

- **Failing Test First**: Start every change by writing a test that fails.
- **Verify Failure**: After writing the test, run it to confirm it fails before implementing.
- **Automatic Test Running**: After every code or test change, run relevant tests using the appropriate Make target. Do not ask for permission.
- **Post-Pass Review**: After a test passes, review for opportunities to simplify or clarify.
- **Clarify Requirements**: If requirements are unclear, ask before writing code or tests.
- **Self-Contained Tests**: Each test must be self-contained and not depend on execution order.
- **Debugging First**: When encountering issues, debug and investigate before asking for help.

## 4. Code Quality Standards

- **Self-Documenting Code**: Avoid comments. Rely entirely on clear naming. Remove comments that describe obvious behavior or duplicate Git history (Arrange/Act/Assert labels, historical references, etc.).
- **Clear Naming**: Use descriptive, purpose-revealing names for all variables, functions, classes, and test functions.
- **Small Components**: Keep classes and methods small. Flag any function exceeding 20 lines.
- **Refactoring Awareness**: Highlight refactoring opportunities and detect repeated code patterns.
- **Graceful Error Handling**: Always implement proper error handling with meaningful messages.
- **Fail Fast**: Design code to fail fast and fail clearly.
- **Input Validation**: Always validate and sanitize external inputs.
- **Secrets Management**: Never hardcode secrets; use proper secret management systems.
- **Security Awareness**: Consider security implications in all design decisions.

## 5. Testing Standards

### Tools & Conventions
- **Test Runner**: Use pytest.
- **Assertion Library**: Use `expects` (BDD style). Use one assertion style consistently throughout the suite.
- **Mocking**: Use doublex and doublex-expects for all application code mocking if the codebase is synchronous. For async codebases, use `unittest.mock` (doublex does not work well with async). Use `@patch` from `unittest.mock` ONLY for Python system modules (readline, atexit, subprocess, sys, os, etc.) regardless of sync/async.
- **Type Hints**: All test functions and helpers must have full type hints.

### Test Quality
- **Focused Tests**: Keep each test under 20 lines.
- **Simple Helpers**: Use helper methods or object mothers/factories for repeated setup. Keep them simple and typed.
- **Complete Coverage**: Ensure every new feature or bugfix has a covering test.
- **Incremental Coverage**: Cover all code paths and edge cases incrementally, one test at a time.
- **Refactor Tests**: Remove duplication and improve readability in test code.
- **Consistent Assertions**: Use `expects` consistently throughout the suite.
- **Test Pyramid**: Write many unit tests, some integration tests, and few acceptance tests.

## 6. Tool Usage & Make Targets

### Core Rule
**NEVER** call tools like `pytest`, `ruff`, `mypy`, or similar directly. Always use the corresponding `make` target.

### Available Make Targets
- `make help` — Show this help.
- `make local-setup` — Setup git hooks and install dependencies.
- `make install` — Install dependencies.
- `make update` — Update dependencies.
- `make add-dep dep="pkg --group X"` — Add a new dependency.
- `make remove-dep dep="pkg --group X"` — Remove a dependency.
- `make test` — Run all tests.
- `make unit` — Run unit tests.
- `make integration` — Run integration tests.
- `make acceptance` — Run acceptance tests.
- `make coverage` — Run tests with coverage report.
- `make check-typing` — Run mypy type checking.
- `make check-lint` — Run ruff linting check.
- `make lint` — Apply ruff linting fixes.
- `make check-format` — Run ruff format check.
- `make format` — Apply ruff format fixes.
- `make watch` — Run tests on every change (watch mode).
- `make up` — Create and start Docker containers.
- `make down` — Stop and remove Docker containers.
- `make run` — Run the application with uvicorn.
- `make migration` — Generate a new alembic migration.
- `make migrate` — Apply alembic migrations.
- `make autostyle` — Apply all code style fixes (format + lint).
- `make show` — Show installed dependencies tree.
- `make search` — Search package details.
- `make audit` — Run security audit on dependencies.
- `make secrets` — Check for secrets in source code.

### Usage Rules
1. **Testing**: Use `make unit`, `make integration` or `make acceptance` as appropriate.
2. **Formatting**: Use `make format` or `make check-format`.
3. **Type Checking**: Use `make check-typing`.
4. **Lint Checks**: Use `make check-lint`.
5. **Help**: If unsure which target to use, run `make help`.
6. **New Operations**: Prefer adding a new Makefile target over running a tool directly.

### Good vs Bad Examples
```sh
# Good: Use make target for unit tests
make unit

# Bad: Call pytest directly
pytest tests
```

## 7. Documentation Standards

- **User-Focused README**: README.md must be user-focused, containing only information relevant to table authors and end users.
- **Separate Dev Docs**: All technical documentation, architectural decisions, and conventions must be maintained in `docs/conventions/`.
- **Separate Specs Docs**: All design decisions, feature specifications, and requirements must be maintained in `docs/features/`.
- **Error Examples**: User-facing documentation should include example error messages for common validation failures to help users quickly resolve issues.

### Repository Structure

| File / Directory           | Content                                                        | When to read                      |
|----------------------------|----------------------------------------------------------------|-----------------------------------|
| `docs/progress/current.md` | Current session state                                          | Always when starting              |
| `docs/progress/history.md` | Logbook — append-only of previous sessions                     | When historic knowledge is needed |
| `docs/features/`           | Feature specs: requirements and acceptance criteria in Gherkin | When implementing a feature       |
| `docs/conventions/`        | Architecture, workflow, and testing conventions                | When coding or reviewing          |
| `instat_python/`           | Source code                                                    | When implementing                 |
| `test/`                    | Automated tests                                                | When implementing and verifying   |

## 8. Quick Reference

1.  Start every response with `**<CONTEMPLATOR>**` 🌲
2.  One test, one file, one change at a time 👣
3.  Failing test first, then implementation ❌➡️✅
4.  Use `make` targets, never tools directly 🔧
5.  Keep everything small and typed 📏
6.  Show thinking conversationally 💭
7.  Question everything ❓
8.  Run tests automatically after every change 🧪
9.  Simplest solution, no abstractions ✨
10. Ask when in doubt 🤔
