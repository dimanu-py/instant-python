.DEFAULT_GOAL := help

.PHONY: help
help:  ## Show this help.
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(firstword $(MAKEFILE_LIST)) | \
			awk 'BEGIN {FS = ":.*## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: test
test:  ## Run all test.
	@{{ general.dependency_manager }} run pytest test -ra

.PHONY: unit
unit:  ## Run all unit test.
	@{{ general.dependency_manager }} run pytest -m "unit" -ra

.PHONY: integration
integration:  ## Run all integration test.
	@{{ general.dependency_manager }} run pytest -m "integration" -ra

.PHONY: acceptance
acceptance:  ## Run all acceptance test.
	@{{ general.dependency_manager }} run pytest -m "acceptance" -ra

.PHONY: coverage
coverage:  ## Run all test with coverage.
	@{{ general.dependency_manager }} run coverage run --branch -m pytest test
	@{{ general.dependency_manager }} run coverage html
	@$(BROWSER) htmlcov/index.html

.PHONY: local-setup
local-setup:  ## Setup git hooks and install dependencies.
	@scripts/local_setup.sh
	@make install

.PHONY: install
install:  ## Install dependencies.
	{% if general.dependency_manager == "uv" %}
	@uv sync --all-groups
	{% elif general.dependency_manager == "pdm" %}
	@pdm install
	{% endif %}

.PHONY: update
update:  ## Update dependencies.
	{% if general.dependency_manager == "uv" %}
	@uv sync --upgrade
	{% elif general.dependency_manager == "pdm" %}
	@pdm update
	{% endif %}

.PHONY: add-dep
add-dep:  ## Add a new dependency.
	@scripts/add_dependency.sh

.PHONY: remove-dep
remove-dep:  ## Remove a dependency.
	@scripts/remove_dependency.sh

.PHONY: check-typing
check-typing:  ## Run mypy type checking.
	@{{ general.dependency_manager }} run mypy

.PHONY: check-lint
check-lint:  ## Run ruff linting check.
	{% if general.dependency_manager == "pdm" %}
	@pdm run ruff check src test
	{% elif general.dependency_manager == "uv" %}
	@uvx ruff check src test
	{% endif %}

.PHONY: lint
lint:  ## Apply ruff linting fix.
	{% if general.dependency_manager == "pdm" %}
	@pdm run ruff check --fix src test
	{% elif general.dependency_manager == "uv" %}
	@uvx ruff check --fix src test
	{% endif %}

.PHONY: check-format
check-format:  ## Run ruff format check.
	{% if general.dependency_manager == "pdm" %}
	@pdm run ruff format --check src test
	{% elif general.dependency_manager == "uv" %}
	@uvx ruff format --check src test
	{% endif %}

.PHONY: format
format:  ## Apply ruff format fix.
	{% if general.dependency_manager == "pdm" %}
	@pdm run ruff format src test
	{% elif general.dependency_manager == "uv" %}
	@uvx ruff format src test
	{% endif %}

.PHONY: pre-commit
pre-commit: check-typing check-lint check-format all-unit ## Run pre-commit checks.

.PHONY: pre-push
pre-push:  all-integration all-acceptance ## Run pre-push checks.

.PHONY: watch
watch:  ## Run all test with every change.
	@{{ general.dependency_manager }} run ptw --runner "pytest -n auto test -ra"

.PHONY: create-aggregate
create-aggregate:  ## Create a new aggregate inside contexts folder.
	@{{ general.dependency_manager }} run python -m scripts.create_aggregate

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
	pdm show $$package
	{% elif general.dependency_manager == "uv" %}
	uv pip show $$package
	{% endif %}

