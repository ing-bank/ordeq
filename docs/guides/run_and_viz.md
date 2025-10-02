# Running and visualizing nodes

The `run` and the `viz` functions are companion tools that allow you to execute and visualize the nodes defined in your code.

## Run

Running nodes with Ordeq is as simple as calling the `run` function from the `ordeq` package:

```python title="main.py"
from ordeq import run, node


@node(inputs=[], outputs=[])
def my_node():
    print("Hello, Ordeq!")


if __name__ == "__main__":
    run(my_node)
```

This function accepts any number of **functions, modules, or packages** as input and will execute the nodes defined within them.
This allows you to adapt the structure of your codebase to the complexity of your project, from single scripts to multi-module packages.

For example, separating nodes into a different module `nodes.py` with identical functionality:

```python title="main.py"
from ordeq import run
import nodes

if __name__ == "__main__":
    run(nodes)
```

```python title="nodes.py"
from ordeq import node


@node(inputs=[], outputs=[])
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
