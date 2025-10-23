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
