from example_imports.catalog import a  # noqa: F401 (unused import)

exec("b = a")  # noqa: S102 (use of exec)
