# Instructions

## Python

Use modern Python coding standards and best practices.
Use pathlib for file operations.

## Documentation

We follow the Google-style docstring convention.
Docstring arguments and return sections should not contain any type information,
as they should already be contained in the type hints of the function.
This also holds for the argument and return descriptions, for example write:

```text
Args:
    packages: package names
```

instead of

```text
Args:
    packages: List of package names
```

When the function returns `None`, the return section should be omitted.
We use type hints for all function arguments and return values.
This applies to code in the `src/` directory, not tests.

Code examples in Python docstrings and markdown must be wrapped in triple backticks with the language "python" or "pycon".
We use `pycon` for interactive examples that include the Python prompt (`>>>`), with at least one printed output.
All other code examples should use `python`.

## Markdown

Markdown headers should use sentence case, not title case.
