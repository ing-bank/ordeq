set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

_default:
    @just --list --unsorted

# Local installation
localsetup: install precommit_install

# Linting and formatting with ruff
ruff: lint format

# Formatting with mdformat
mdformat:
    uv run --with mdformat-mkdocs mdformat --check docs/ README.md

# Fix formatting with mdformat
mdformat-fix:
    uv run --with mdformat-mkdocs mdformat docs/ README.md

# Formatting with ruff via doccmd
doccmd-ruff-format:
    uv run --with doccmd doccmd --language=python --no-pad-file --no-pad-groups --command="ruff format --quiet" docs/ README.md

# Linting with ruff via doccmd
doccmd-ruff-lint:
    uv run --with doccmd doccmd --language=python --no-pad-file --no-pad-groups --command="ruff check --quiet --fix" docs/ README.md

# Combine doccmd with ruff for linting and formatting
doccmd-fix: doccmd-ruff-format doccmd-ruff-lint

# Linting with ruff
lint:
    uv run --group lint ruff check packages/ scripts/ examples/

# Fix linting issues with ruff
lint-fix:
    uv run --group lint ruff check --fix packages/ scripts/ examples/

# Formatting with ruff
format:
    uv run --group lint ruff format --check packages/ scripts/ examples/

# Fix formatting with ruff
format-fix:
    uv run --group lint ruff format packages/ scripts/ examples/

# Type checking with ty
ty:
    uv run --group types ty check packages/ scripts/

# List all packages
list:
    ls -1 packages/

# Type checking with mypy
mypy: mypy-packages mypy-examples

# Mypy check all package directories
mypy-packages:
    for dir in `find packages -maxdepth 1 -type d -name "ordeq*"`; do \
            uv run --group types mypy --check-untyped-defs --follow-untyped-imports $dir/src || exit 1; \
    done

# Mypy check all example directories
mypy-examples:
    for dir in `find examples/ -mindepth 1 -maxdepth 1 -type d`; do \
        uv run --group types mypy --check-untyped-defs --follow-untyped-imports $dir/src || exit 1; \
    done

# Static analysis (lint + type checking)
sa: ruff ty mypy

# Format code and apply lint fixes with ruff and mdformat
fix: format-fix lint-fix mdformat-fix doccmd-fix

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

# Generate API documentation pages
generate-api-docs:
    uv run scripts/generate_api_docs.py

# Generate package overview documentation page
generate-package-overview:
    uv run scripts/generate_package_overview.py

# Build the documentation
docs-build: generate-api-docs generate-package-overview
    uv run --group docs mkdocs build --strict

# Build and serve the documentation locally
docs-serve: generate-api-docs generate-package-overview
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

# Build a package
build PACKAGE:
    echo "prune tests" > ./packages/{{ PACKAGE }}/MANIFEST.in || true
    cp -n ./README.md ./packages/{{ PACKAGE }}/README.md || true
    cp -n ./LICENSE ./packages/{{ PACKAGE }}/LICENSE || true
    cp -n ./NOTICE ./packages/{{ PACKAGE }}/NOTICE || true
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

# Delete all .snapshot.md files anywhere in the repository
delete-snapshots:
    find . -type f -name "*.snapshot.md" -delete

# Recompute snapshots by running only those tests for all packages
capture-snapshots:
    for dir in `find packages -type d -name "ordeq*" -maxdepth 1`; do \
        uv run --group test pytest $dir -v -m snapshot || [ $? -eq 5 ]; \
    done \
