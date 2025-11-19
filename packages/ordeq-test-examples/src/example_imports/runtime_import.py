# ruff: noqa: F401 (unused import)
import importlib

from example_imports.catalog import a

module = importlib.import_module("example_imports.catalog")
b = module.a
