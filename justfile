_default:
    @just --list --unsorted

# Local installation
localsetup: install precommit_install

# Linting and formatting with ruff
ruff: lint format

mdformat:
    uv run --with mdformat-mkdocs --with mdformat-ruff --with ruff mdformat --check docs/ README.md || exit 1

# Linting with ruff
lint:
    uv run --group lint ruff check packages/ scripts/ || exit 1

# Formatting with ruff
format:
    uv run --group lint ruff format --check packages/ scripts/ || exit 1

# Type checking with ty
ty:
    uv run --group types ty check packages/ scripts/ || exit 1

# Type checking with mypy
mypy:
    for dir in `find packages -maxdepth 1 -type d -name "ordeq*"`; do \
        uv run --group types mypy --check-untyped-defs --follow-untyped-imports $dir/src || exit 1; \
    done


# Static analysis (lint + type checking)
sa: ruff ty mypy

# Format code and apply lint fixes with ruff and mdformat
fix:
    uv run --group lint ruff format packages/ scripts/ || exit 1
    uv run --group lint ruff check --fix packages/ scripts/ || exit 1
    uv run --with mdformat-mkdocs --with mdformat-ruff mdformat docs/ README.md

# Test all packages individually
# or test specific ones by passsing the names as arguments
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

# Build the documentation
docs-build:
    uv run scripts/generate_api_docs.py
    uv run --group docs mkdocs build --strict

# Build and serve the documentation locally
docs-serve:
    uv run scripts/generate_api_docs.py
    uv run --group docs mkdocs serve --strict

# Publish the documentation to GitHub Pages
docs-publish:
    uv run scripts/generate_api_docs.py
    uv run --group docs mkdocs build --strict
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

# Publish a package to PyPI
# Required when the package is first released.
# You need an API token from PyPI to run this command.
publish PACKAGE:
    uv build --package {{ PACKAGE }} --sdist
    uv publish

# Lock dependencies
lock:
    uv lock

# Bump version
bump *ARGS:
    uv run scripts/next_tag.py {{ ARGS }} || exit 1
