We follow the Google-style docstring convention.
Docstring arguments and return sections should not contain any type information,
as they should already be contained in the type hints of the function.
When the function returns `None`, the return section should be omitted.
We use type hints for all function arguments and return values.

Code examples in Python docstrings and markdown must be wrapped in triple backticks with the language "python" or "pycon".
We use `pycon` for interactive examples that include the Python prompt (`>>>`), with at least one printed output.
All other code examples should use `python`.
