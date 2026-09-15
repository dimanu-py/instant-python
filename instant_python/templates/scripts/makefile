{% set has_pre_commit_hooks = "precommit_hook" in template.built_in_features %}
{% set has_github_actions_or_makefile = ["github_actions", "makefile"] | is_in(template.built_in_features) %}
{% set has_agents = "ai_agents" in template.built_in_features %}
{% set has_custom_docs = "custom_documentation" in template.built_in_features %}
.DEFAULT_GOAL := help

.PHONY: help
help:  ## Show this help.
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(firstword $(MAKEFILE_LIST)) | \
			awk 'BEGIN {FS = ":.*## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: local-setup
local-setup:  ## Setup git hooks and install dependencies.
	@echo "⌛ Setting up the project...\n"
	@make install
{% if has_pre_commit_hooks %}
	@uv run -m pre_commit install --hook-type pre-commit --hook-type commit-msg --hook-type pre-push
{% endif %}

.PHONY: install
install:  ## Install dependencies.
	@echo "⌛ Installing dependencies...\n"
	@uv sync --all-groups

.PHONY: update
update:  ## Update dependencies.
	@echo "⌛ Updating dependencies...\n"
	@uv lock --upgrade
	@uv sync --all-groups

.PHONY: add-dep
add-dep:  ## Add a new dependency
	@uv add $(dep)

.PHONY: remove-dep
remove-dep:  ## Remove a dependency
	@uv remove $(dep)

{% if dependencies | has_dependency("pytest") or has_github_actions_or_makefile %}
.PHONY: test
test:  ## Run all tests (optional: TESTS_PATH=tests/module/).
	@echo "⌛ Running tests...\n"
	@uv run pytest $(or $(TESTS_PATH),test) -ra

.PHONY: unit
unit:  ## Run all unit test (optional: TESTS_PATH=tests/module/).
	@echo "⌛ Running unit tests...\n"
	@uv run pytest -m "unit" $(TESTS_PATH) -ra

.PHONY: integration
integration:  ## Run all integration test (optional: TESTS_PATH=tests/module/).
	@echo "⌛ Running integration tests...\n"
	@uv run pytest -m "integration" $(TESTS_PATH) -ra

.PHONY: acceptance
acceptance:  ## Run all acceptance test (optional: TESTS_PATH=tests/module/).
	@echo "⌛ Running acceptance tests...\n"
	@uv run pytest -m "acceptance" $(TESTS_PATH) -ra

.PHONY: coverage
coverage:  ## Run all test with coverage.
	@echo "⌛ Running tests with coverage...\n"
	@uv run coverage run --branch -m pytest test
	@uv run coverage html
	@$(BROWSER) htmlcov/index.html
{% endif %}
{% if dependencies | has_dependency("pytest-watch") %}
.PHONY: watch
watch:  ## Run all test with every change.
	@echo "⌛ Running test in watch mode...\n"
	@uv run ptw --runner "pytest test -ra"
{% endif %}

.PHONY: check-typing
check-typing:  ## Run mypy type checking.
	@echo "⌛ Running type checking...\n"
{% if dependencies | has_dependency("mypy") or has_github_actions_or_makefile %}
	@uv run mypy
{% elif dependencies | has_dependency("ty") or has_github_actions_or_makefile %}
	@uv run ty
{% elif dependencies | has_dependency("pyright") or has_github_actions_or_makefile %}
	@uv run pyright
{% elif dependencies | has_dependency("pyrefly") or has_github_actions_or_makefile %}
	@uv run pyrefly
{% endif %}

{% if dependencies | has_dependency("ruff") or has_github_actions_or_makefile or has_pre_commit_hooks %}
.PHONY: check-lint
check-lint:  ## Run ruff linting check.
	@echo "⌛ Running linting check...\n"
	@uvx ruff check src test

.PHONY: lint
lint:  ## Apply ruff linting fix.
	@echo "\n⌛ Applying linting fixes...\n"
	@uvx ruff check --fix src test

.PHONY: check-format
check-format:  ## Run ruff format check.
	@echo "⌛ Checking code formatting...\n"
	@uvx ruff format --check src test

.PHONY: format
format:  ## Apply ruff format fix.
	@echo "⌛ Formatting project code...\n"
	@uvx ruff format src test

.PHONY: autostyle
autostyle:  ## Apply all code style fixes.
	@echo "\n⌛ Applying all code style fixes...\n"
	@make format
	@make lint
	@git add . && git commit -m "style: apply code style fixes"
{% endif %}
{% if has_pre_commit_hooks %}
.PHONY: secrets
secrets: # Check for secrets in the source code
	@echo "⌛ Checking secrets...\n"
	@uv run -m pre_commit run gitleaks --all-files
{% endif %}

{% if "github_actions" in template.built_in_features %}
.PHONY: audit
audit: # It audits dependencies and source code
	@echo "⌛ Checking for vulnerabilities in dependencies...\n"
	@uv run -m pip_audit --progress-spinner off
{% endif %}

.PHONY: clean
clean: # Clean up the project, removing the virtual environment and some files
	@echo "\n⌛ Cleaning up the project...\n"

	@uv run -m pre_commit clean)
	@uv run -m pre_commit uninstall --hook-type pre-commit --hook-type commit-msg)
	@rm --force --recursive .venv
	@rm --force --recursive `find . -type f -name '*.py[co]'`
	@rm --force --recursive `find . -name __pycache__`
	@rm --force --recursive `find . -name .ruff_cache`
	@rm --force --recursive `find . -name .mypy_cache`
	@rm --force --recursive `find . -name .pytest_cache`
	@rm --force --recursive .coverage
	@rm --force --recursive .coverage.*
	@rm --force --recursive coverage.xml
	@rm --force --recursive htmlcov

.PHONY: show
show:  ## Show installed dependencies.
	@uv tree

.PHONY: search
search:  ## Show package details.
	@read -p "Enter package name to search: " package;\
	@uv pip show $$package
{% if has_agents %}
.PHONY: claude
claude:  ## Create symlinks for Claude Code compatibility (CLAUDE.md → AGENTS.md, .claude → .agents).
	@echo "\n⌛ Creating Claude Code symlinks...\n"
	@ln -sf AGENTS.md CLAUDE.md
	@ln -sfn .agents .claude
	@ls -la CLAUDE.md .claude

.PHONY: opencode
opencode:  ## Create symlinks for OpenCode compatibility.
	@echo "\n⌛ Creating OpenCode symlinks...\n"
	@mkdir -p .opencode
	@rm -rf .opencode/commands
	@ln -s ../.agents/commands .opencode/commands
	@ln -s ../.agents/agents .opencode/agents
	@ls -la .opencode

.PHONY: mutate
mutate:  ## Run mutation testing (optional: MUTATE_PATH="{{ general.source_name }}.<module>.*", dotted module pattern).
	@echo "⌛ Running mutation testing...\n"
	@{{ general.dependency_manager }} run mutmut run $(or $(MUTATE_PATH),{{ general.source_name }})
	@{{ general.dependency_manager }} run mutmut results
{% endif %}
{% if has_custom_docs %}
.PHONY: docs-serve
docs-serve:  ## Start server for documentation.
	@uv run mkdocs serve
{% endif %}