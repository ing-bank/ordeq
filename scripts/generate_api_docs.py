"""Generates the content of the 'docs/api/' directory, mirroring the content
of 'packages/*/src'. Creates a Markdown file for each Python module (except
some special ones like __init__). Each Markdown file contains a reference to
the Python module. `mkdocstrings` then picks up the reference and generates
the Markdown file content based on the string docs in the module.

More info: https://mkdocstrings.github.io/ .

Note: there are existing MkDocs plugins available that achieve something
similar, but I find these unnecessary for our use case.
"""

from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
PACKAGES_DIR = ROOT_DIR / "packages"
PACKAGE_DIRS = PACKAGES_DIR.glob("*")
DOCS_DIR = ROOT_DIR / "docs"
API_DIR = DOCS_DIR / "api"

for package_dir in sorted(PACKAGE_DIRS):
    package_src = package_dir / "src"
    package_name = package_dir.parts[-1]
    for module in sorted(package_src.rglob("*.py")):
        module_path = module.relative_to(package_src).with_suffix("")
        full_doc_path = API_DIR / module_path.with_suffix(".md")

        full_doc_path.parent.mkdir(parents=True, exist_ok=True)

        parts = tuple(module_path.parts)

        if parts[-1] in {"__main__", "_version", "__init__"}:
            continue

        module_name = parts[-1]

        with full_doc_path.open(mode="w") as fh:
            print(f"---\ntitle: {module_name}.py\n---", file=fh)
            identifier = ".".join(parts)
            print("::: " + identifier, file=fh)
