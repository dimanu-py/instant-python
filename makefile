.DEFAULT_GOAL := help

.PHONY: help
help:  ## Show this help.
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(firstword $(MAKEFILE_LIST)) | \
			awk 'BEGIN {FS = ":.*## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: local-setup
local-setup:  ## Setup git hooks and install dependencies.
	@echo "\n⌛ Setting up the project...\n"
	@make install
	@uv run -m pre_commit install --hook-type pre-commit --hook-type commit-msg --hook-type pre-push
	@echo "\n✅ Run 'source .venv/bin/activate' to activate the virtual environment.\n"

.PHONY: test
test:  ## Run all test.
	@echo "\n⌛ Running tests...\n"
	@uv run pytest test -ra
	@echo "\n✅ Test passed.\n"

.PHONY: coverage
coverage:  ## Run all test with coverage.
	@echo "\n⌛ Running tests with coverage...\n"
	@uv run coverage run --branch -m pytest test
	@uv run coverage html
	@$(BROWSER) htmlcov/index.html
	@echo "\n✅ Coverage report generated at htmlcov/index.html.\n"

.PHONY: install
install:  ## Install dependencies.
	@echo "\n⌛ Installing dependencies...\n"
	@uv sync --all-groups
	@echo "\n✅ Dependencies installed correctly.\n"

.PHONY: update
update:  ## Update dependencies.
	@echo "\n⌛ Updating dependencies...\n"
	@uv sync --upgrade
	@echo "\n✅ Dependencies updated correctly.\n"

.PHONY: add-dep
add-dep:  ## Add a new dependency.
	@uv run scripts/add_dependency.py

.PHONY: remove-dep
remove-dep:  ## Remove a dependency.
	@uv run scripts/remove_dependency.py

.PHONY: check-typing
check-typing:  ## Run mypy type checking.
	@echo "\n⌛ Running type checking with mypy...\n"
	@uv run mypy
	@echo "\n✅ Type checking completed.\n"

.PHONY: check-lint
check-lint:  ## Run ruff linting check.
	@echo "\n⌛ Running linting check...\n"
	@uvx ruff check instant_python test
	@echo "\n✅ Linting check completed.\n"

.PHONY: lint
lint:  ## Apply ruff linting fix.
	@echo "\n⌛ Applying linting fixes...\n"
	@uvx ruff check --fix instant_python test
	@echo "\n✅ Linting fixes applied.\n"

.PHONY: check-format
check-format:  ## Run ruff format check.
	@echo "\n⌛ Checking code formatting...\n"
	@uvx ruff format --check instant_python test
	@echo "\n✅ Code formatting check completed.\n"

.PHONY: format
format:  ## Apply ruff format fix.
	@echo "\n⌛ Formatting project code...\n"
	@uvx ruff format instant_python test
	@echo "\n✅ Code formatted correctly.\n"

.PHONY: watch
watch:  ## Run all test with every change.
	@uv run ptw --runner "pytest -n auto test -ra"

.PHONY: show
show:  ## Show installed dependencies.
	@uv tree

.PHONY: search
search:  ## Show package details.
	@read -p "Enter package name to search: " package;\
	uv pip show $$package

.PHONY: tox
tox:  ## Run tox tests
	@uv run tox

.PHONY: audit
audit: # It audits dependencies and source code
	@echo "\n⌛ Running security audit...\n"
	@uv run -m pip_audit --progress-spinner off
	@echo "\n✅ Security audit completed correctly.\n"

.PHONY: secrets
secrets: # It checks for secrets in the source code
	@echo "\n⌛ Checking secrets...\n"
	@uv run -m pre_commit run gitleaks --all-files
	@echo "\n✅ Secrets checked correctly.\n"

.PHONY: build
build:  ## Build the project.
	@echo "\n⌛ Building the project...\n"
	@uv build
	@echo "\n✅ Project built successfully.\n"

.PHONY: clean
clean: # It cleans up the project, removing the virtual environment and some files
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

	@echo "\n✅ Run 'deactivate' to deactivate the virtual environment.\n"

.PHONY: docs-serve
docs-serve:  ## Start server for documentation.
	@uv run mkdocs serve