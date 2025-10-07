set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

_default:
    @just --list --unsorted

# Local installation
localsetup: install precommit_install

# Linting and formatting with ruff
ruff: lint format

# Formatting with mdformat
mdformat:
    uv run --with mdformat-mkdocs --with mdformat-ruff --with ruff mdformat --check docs/ README.md

mdformat-fix:
    uv run --with mdformat-mkdocs --with mdformat-ruff mdformat docs/ README.md

# Linting with ruff
lint:
    uv run --group lint ruff check packages/ scripts/

lint-fix:
    uv run --group lint ruff check --fix packages/ scripts/

# Formatting with ruff
format:
    uv run --group lint ruff format --check packages/ scripts/

format-fix:
    uv run --group lint ruff format packages/ scripts/

# Type checking with ty
ty:
    uv run --group types ty check packages/ scripts/

# List all packages
list:
    ls -1 packages/

# Type checking with mypy
mypy:
    for dir in `find packages -maxdepth 1 -type d -name "ordeq*"`; do \
        uv run --group types mypy --check-untyped-defs --follow-untyped-imports $dir/src || exit 1; \
    done

# Static analysis (lint + type checking)
sa: ruff ty mypy

# Format code and apply lint fixes with ruff and mdformat
fix: format-fix lint-fix mdformat-fix

# Test all packages individually
# or test specific ones by passing the names as arguments
# eg. `just test` (Run tests in all packages)

# or `just test ordeq ordeq-cli-runner` (Run tests in the 'ordeq' and 'ordeq-cli-runner' packages)
test *PACKAGES:
    if [ -z "{{ PACKAGES }}" ]; then \
        for dir in `find packages -type d -name "ordeq*" -maxdepth 1`; do \
            uv run --group test pytest $dir -v || exit 1; \
        done \
    else \
        for package in {{ PACKAGES }}; do \
            uv run --group test pytest packages/$package -v || exit 1; \
        done \
    fi

# Test a single package
test_package PACKAGE:
    uv run --group test pytest packages/{{ PACKAGE }} -v

# Run tests for all packages with coverage
test_all:
    uv run --group test pytest packages/ --cov=packages/ --cov-report=html

generate-api-docs:
    uv run scripts/generate_api_docs.py

# Build the documentation
docs-build: generate-api-docs
    uv run --group docs mkdocs build --strict

# Build and serve the documentation locally
docs-serve: generate-api-docs
    uv run --group docs mkdocs serve --strict

# Publish the documentation to GitHub Pages
docs-publish: docs-build
    uv run --group docs mkdocs gh-deploy --force

# Run pre-commit hooks
precommit:
    uv run pre-commit run --all-files

# Install pre-commit hooks
precommit_install:
    uv run pre-commit install

# Install development dependencies
install:
    uv sync --all-packages --all-groups --all-extras

# Upgrade (pre-commit only)
upgrade:
    # TODO: keep an eye out for: https://github.com/astral-sh/uv/issues/6794
    pre-commit autoupdate

build PACKAGE:
    cp -n ./README.md ./packages/{{ PACKAGE }}/README.md || true
    cp -n ./README.md ./packages/{{ PACKAGE }}/LICENSE || true
    uv build --package {{ PACKAGE }}

# You need an API token from PyPI to run this command.
publish PACKAGE:
    just build {{ PACKAGE }}
    uv publish

# Lock dependencies
lock:
    uv lock

# Bump version
bump *ARGS:
    uv run scripts/next_tag.py {{ ARGS }}
