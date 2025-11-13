# Running and visualizing nodes

The `run` and the `viz` functions are companion tools that allow you to execute and visualize the nodes defined in your code.

## Run

Running nodes with Ordeq is as simple as calling the `run` function from the `ordeq` package:

```python title="main.py"
from ordeq import run, node


@node
def my_node():
    print("Hello, Ordeq!")


if __name__ == "__main__":
    run(my_node)
```

This function accepts any number of **functions, modules, or packages** as input and will execute the nodes defined within them.
This allows you to adapt the structure of your codebase to the complexity of your project.
For small projects, you might keep everything in a single script.
To run all nodes defined in that script, simply pass the module itself to `run`:

```python title="main.py"
from ordeq import run, node


@node
def my_node():
    print("Hello, Ordeq!")


if __name__ == "__main__":
    run(__name__)
```

For larger projects, you can organize your nodes into separate modules or packages.
For example, separating nodes into a different module `nodes.py` with identical functionality:

```python title="main.py"
from ordeq import run
import nodes

if __name__ == "__main__":
    run(nodes)
```

```python title="nodes.py"
from ordeq import node


@node
def my_node():
    print("Hello, Ordeq!")
```

### Modular pipelines

You can run pipelines multiple times with different inputs using `run`.
We refer to this as modular pipelines.
This is particularly useful when you want to reuse a pipeline for different data or configurations without duplicating code.

For example, Ordeq uses this pattern in the `ordeq_dev_tools` package to generate release notes for multiple packages:

```python title="main.py"
from ordeq import node, run

from ordeq_common import StringBuffer, Literal

from ordeq_dev_tools.pipelines.shared import packages
from ordeq_dev_tools.pipelines import generate_release_notes  # The pipeline to reuse

@node(inputs=[packages])  # packages are dynamically provided
def new_releases(package_names: list[str]) -> dict[str, str]:
    new_release_data = {}
    for package_name in package_names:
        # The new tag and release notes will be captured as strings here
        new_tag = StringBuffer()
        notes = StringBuffer()

        try:
            run(
                generate_release_notes,
                # Map the placeholder IOs to the specific IOs for this iteration
                io={
                    generate_release_notes.package: Literal(package_name),
                    generate_release_notes.release_notes: notes,
                    generate_release_notes.new_tag: new_tag,
                },
            )
            # Store the results in the dictionary
            new_release_data[new_tag.load()] = notes.load()
        # We crafted the nodes in the pipelines so that anywhere we know
        # that there is no new release, a ValueError is raised.
        except ValueError:
            print(f"No new release for package {package_name}")

    return new_release_data
```

What is happening here is that for each package name in `package_names`, the `run` function is called with the `generate_release_notes` pipeline.
The `io` argument is used to provide specific inputs to the nodes within that pipeline, replacing the placeholders in `generate_release_notes`.
This allows the same pipeline to be executed multiple times with different inputs, creating clarity and modularity in the code.

### Logging

By default, Ordeq logs execution progress using the `INFO` level.
The default Python logging level is `WARNING`, so to see Ordeq logs, you need to set the logging level to `INFO` or lower:

```python title="main.py"
import logging
from ordeq import run
import nodes

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    run(nodes)
```

## Viz

The `viz` function from the `ordeq_viz` package allows you to visualize the nodes and their dependencies in a graph format:

```python title="main.py"
from pathlib import Path
from ordeq_viz import viz
import nodes

if __name__ == "__main__":
    viz(nodes, fmt="mermaid", output=Path("pipeline.mermaid"))
```

Just as `run`, the `viz` function accepts **functions, modules, or packages** as input and will generate a visual representation of the nodes and their dependencies.

### Notebooks

In notebook environments, you can directly visualize the graph without saving it to a file:

```python title="notebook.ipynb"
from ordeq_viz import viz
from IPython.display import display, Markdown
import nodes

diagram = viz(nodes, fmt="mermaid")
display(Markdown(diagram))
```

Jupyter supports this [since version 7.1](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#diagrams-in-markdown).

Similarly for Marimo notebooks, you can display the diagram directly:

```python title="notebook.py"
from ordeq_viz import viz
import nodes
import marimo as mo

diagram = viz(nodes, fmt="mermaid")
mo.mermaid(diagram)
```

## Combining run and viz

You can also combine both `run` and `viz` in a single script to execute the nodes and visualize the workflow:

```python title="main.py"
from pathlib import Path
from ordeq import run
from ordeq_viz import viz
import nodes

if __name__ == "__main__":
    run(nodes)
    viz(nodes, fmt="mermaid", output=Path("pipeline.mermaid"))
```

This is particularly powerful for debugging and understanding complex workflows.

!!! note "Split screen development"

    Split screen view in your IDE is very handy for working with source code, `run` and `viz` outputs side by side.
