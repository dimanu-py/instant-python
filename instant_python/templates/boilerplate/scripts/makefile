.DEFAULT_GOAL := help

.PHONY: help
help:  ## Show this help.
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(firstword $(MAKEFILE_LIST)) | \
			awk 'BEGIN {FS = ":.*## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: local-setup
local-setup:  ## Setup git hooks and install dependencies.
	@echo "⌛ Setting up the project...\n"
	@make install
{% if "precommit_hook" in template.built_in_features %}
	@uv run -m pre_commit install --hook-type pre-commit --hook-type commit-msg --hook-type pre-push
{% else %}
	@uv run scripts/local_setup.py
{% endif %}

.PHONY: install
install:  ## Install dependencies.
	@echo "⌛ Installing dependencies...\n"
	{% if general.dependency_manager == "uv" %}
	@uv sync --all-groups
	{% elif general.dependency_manager == "pdm" %}
	@pdm install
	{% endif %}

.PHONY: update
update:  ## Update dependencies.
	@echo "⌛ Updating dependencies...\n"
	{% if general.dependency_manager == "uv" %}
	@uv sync --upgrade
	{% elif general.dependency_manager == "pdm" %}
	@pdm update
	{% endif %}

.PHONY: add-dep
add-dep:  ## Add a new dependency <make add-dep dep="pytest --group test>"
	@uv add $(dep)

.PHONY: remove-dep
remove-dep:  ## Remove a dependency <make remove-dep dep="pytest --group test">
	@uv remove $(dep)

{% if dependencies | has_dependency("pytest") or ["github_actions", "makefile"] | is_in(template.built_in_features) %}
.PHONY: test
test:  ## Run all test.
	@echo "⌛ Running tests...\n"
	@{{ general.dependency_manager }} run pytest test -ra

.PHONY: unit
unit:  ## Run all unit test.
	@echo "⌛ Running unit tests...\n"
	@{{ general.dependency_manager }} run pytest -m "unit" -ra

.PHONY: integration
integration:  ## Run all integration test.
	@echo "⌛ Running integration tests...\n"
	@{{ general.dependency_manager }} run pytest -m "integration" -ra

.PHONY: acceptance
acceptance:  ## Run all acceptance test.
	@echo "⌛ Running acceptance tests...\n"
	@{{ general.dependency_manager }} run pytest -m "acceptance" -ra

.PHONY: coverage
coverage:  ## Run all test with coverage.
	@echo "⌛ Running tests with coverage...\n"
	@{{ general.dependency_manager }} run coverage run --branch -m pytest test
	@{{ general.dependency_manager }} run coverage html
	@$(BROWSER) htmlcov/index.html
{% endif %}

{% if dependencies | has_dependency("pytest-watch") %}
.PHONY: watch
watch:  ## Run all test with every change.
	@echo "⌛ Running test in watch mode...\n"
	@{{ general.dependency_manager }} run ptw --runner "pytest test -ra"
{% endif %}

.PHONY: check-typing
check-typing:  ## Run mypy type checking.
	@echo "⌛ Running type checking...\n"
{% if dependencies | has_dependency("mypy") or ["github_actions", "makefile"] | is_in(template.built_in_features) %}
	@{{ general.dependency_manager }} run mypy
{% elif dependencies | has_dependency("ty") or ["github_actions", "makefile"] | is_in(template.built_in_features) %}
	@{{ general.dependency_manager }} run ty
{% elif dependencies | has_dependency("pyright") or ["github_actions", "makefile"] | is_in(template.built_in_features) %}
	@{{ general.dependency_manager }} run pyright
{% elif dependencies | has_dependency("pyrefly") or ["github_actions", "makefile"] | is_in(template.built_in_features) %}
	@{{ general.dependency_manager }} run pyrefly
{% endif %}

{% if dependencies | has_dependency("ruff") or ["github_actions", "makefile"] | is_in(template.built_in_features) %}
.PHONY: check-lint
check-lint:  ## Run ruff linting check.
	@echo "⌛ Running linting check...\n"
	{% if general.dependency_manager == "pdm" %}
	@pdm run ruff check src test
	{% elif general.dependency_manager == "uv" %}
	@uvx ruff check src test
	{% endif %}

.PHONY: lint
lint:  ## Apply ruff linting fix.
	@echo "\n⌛ Applying linting fixes...\n"
	{% if general.dependency_manager == "pdm" %}
	@pdm run ruff check --fix src test
	{% elif general.dependency_manager == "uv" %}
	@uvx ruff check --fix src test
	{% endif %}

.PHONY: check-format
check-format:  ## Run ruff format check.
	@echo "⌛ Checking code formatting...\n"
	{% if general.dependency_manager == "pdm" %}
	@pdm run ruff format --check src test
	{% elif general.dependency_manager == "uv" %}
	@uvx ruff format --check src test
	{% endif %}

.PHONY: format
format:  ## Apply ruff format fix.
	@echo "⌛ Formatting project code...\n"
	{% if general.dependency_manager == "pdm" %}
	@pdm run ruff format src test
	{% elif general.dependency_manager == "uv" %}
	@uvx ruff format src test
	{% endif %}
{% endif %}

{% if "precommit_hook" in template.built_in_features %}
.PHONY: secrets
secrets: # Check for secrets in the source code
	@echo "⌛ Checking secrets...\n"
	@uv run -m pre_commit run gitleaks --all-files
{% else %}
.PHONY: pre-commit
pre-commit: check-typing check-lint check-format all-unit ## Run pre-commit checks.

.PHONY: pre-push
pre-push:  all-integration all-acceptance ## Run pre-push checks.
{% endif %}

{% if "github_actions" in template.built_in_features %}
.PHONY: audit
audit: # It audits dependencies and source code
	@echo "⌛ Checking for vulnerabilities in dependencies...\n"
	@{{ general.dependency_manager }} run -m pip_audit --progress-spinner off
{% endif %}

.PHONY: clean
clean: # Clean up the project, removing the virtual environment and some files
	@echo "\n⌛ Cleaning up the project...\n"

	@{{ general.dependency_manager }} run -m pre_commit clean)
	@{{ general.dependency_manager }} run -m pre_commit uninstall --hook-type pre-commit --hook-type commit-msg)
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
	{% if general.dependency_manager == "pdm" %}
	@pdm list
	{% elif general.dependency_manager == "uv" %}
	@uv tree
	{% endif %}

.PHONY: search
search:  ## Show package details.
	@read -p "Enter package name to search: " package;\
	{% if general.dependency_manager == "pdm" %}
	@pdm show $$package
	{% elif general.dependency_manager == "uv" %}
	@uv pip show $$package
	{% endif %}

