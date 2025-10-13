"""Generates the content of the 'docs/api/' directory, mirroring the content
of 'packages/*/src'. Creates a Markdown file for each Python module (except
some special ones like __init__). Each Markdown file contains a reference to
the Python module. `mkdocstrings` then picks up the reference and generates
the Markdown file content based on the string docs in the module.

More info: https://mkdocstrings.github.io/ .

Note: there are existing MkDocs plugins available that achieve something
similar, but I find these unnecessary for our use case.
"""

import shutil
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
PACKAGES_DIR = ROOT_DIR / "packages"
PACKAGE_DIRS = PACKAGES_DIR.glob("*")
DOCS_DIR = ROOT_DIR / "docs"
API_DIR = DOCS_DIR / "api"


def clear_api_docs() -> None:
    """Clear the API_DIR, retaining .nav.yml and .gitignore files.

    Removes all files and directories in API_DIR except for .nav.yml and
    .gitignore. Creates API_DIR if it does not exist.
    """
    API_DIR.mkdir(parents=True, exist_ok=True)
    for item in API_DIR.iterdir():
        if item.name in {".nav.yml", ".gitignore"}:
            continue
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()


def generate_api_docs():
    for package_dir in sorted(PACKAGE_DIRS):
        package_src = package_dir / "src"
        for module in sorted(package_src.rglob("*.py")):
            module_path = module.relative_to(package_src).with_suffix("")
            parts = tuple(module_path.parts)

            if parts[-1] in {"__main__", "_version", "__init__"}:
                continue

            module_name = parts[-1]
            # Avoid reserved name 'index.md' in MkDocs (ordeq-faiss/index.py)
            if module_name == "index":
                output_name = "index_module"
            else:
                output_name = module_name

            full_doc_path = API_DIR / module_path.with_name(
                f"{output_name}.md"
            )
            full_doc_path.parent.mkdir(parents=True, exist_ok=True)

            with full_doc_path.open(mode="w") as fh:
                print(f"---\ntitle: {module_name}.py\n---", file=fh)
                identifier = ".".join(parts)
                print("::: " + identifier, file=fh)


def generate_api_readmes() -> None:
    """Generate a README.md in each top-level docs/api/*/ directory.

    The README.md will contain a Markdown H1 title using the directory name.
    """
    for subdir in API_DIR.iterdir():
        if subdir.is_dir():
            readme = subdir / "README.md"
            title = f"# {subdir.name}\n"
            readme.write_text(title, encoding="utf-8")


if __name__ == "__main__":
    print("Generating API docs...")
    clear_api_docs()
    generate_api_docs()
    generate_api_readmes()
