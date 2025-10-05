# Node parameters

Passing parameters to nodes is a powerful way to customize their behavior without modifying the node's code.
In Ordeq, parameters are just native IOs and need not be treated differently than regular inputs and outputs.

Commonly used parameter types that are supported out of the box include:

- Python built-in types: `str`, `int`, `float`, `bool`
- Configuration files (TOML, YAML, JSON, INI, etc.)
- Pydantic models
- CLI arguments or environment variables

## Using IOs instead of global variables

Although it is possible to use global variables for parameters, it is not recommended.
Using IOs has several advantages:

- **Clarity**: It is clear which parameters a node depends on. The parameters are included in `run` and `viz` outputs.
- **Maintainability**: Configuration and transformations are separated, making it easier to change one without affecting the other. For example, we could easily change the a parameter to be read from a configuration file or CLI argument.
- **Reproducibility**: When the behavior of a node is fully determined by its inputs, this makes it easier to reproduce results and avoid unintended side effects. Moreover, this means Ordeq can avoid recomputation when the inputs have not changed.

Example using global variables (not recommended):

```python
from ordeq import node, IO
from ordeq_common import Static, StringBuffer

name_str = StringBuffer("John")
greeting = IO()
excited = False


@node(inputs=name_str, outputs=greeting)
def greet(name: str) -> str:
    message = f"Hello, {name}"
    if excited:
        message += "!"
    return message
```

Instead, use an IO for the `excited` parameter:

```python
from ordeq import node, IO
from ordeq_common import Static, StringBuffer

name_str = StringBuffer("John")
greeting = IO()
is_excited = Static(False)


@node(inputs=[name_str, is_excited], outputs=greeting)
def greet(name: str, excited: bool) -> str:
    message = f"Hello, {name}"
    if excited:
        message += "!"
    return message
```

This way, the `greet` node is fully defined by its inputs and outputs, for instance making it possible to avoid recomputation when the inputs have not changed.

## Reading from a `pyproject.toml` section

The pyproject.toml format is the standard way to configure Python projects.
The [`[tool]`](https://packaging.python.org/en/latest/specifications/pyproject-toml/#pyproject-tool-table) table is intended for tool-specific configuration.
Ordeq can read parameters from a `[tool.your_tool_name]` section in `pyproject.toml` and pass it to one or more nodes using little code.

```python
from typing import Any
from pathlib import Path
from ordeq import node, IO
from ordeq_pyproject import Pyproject


name = IO()
pyproject = Pyproject(path=Path("pyproject.toml"), section="tool.my_tool")
greeting = IO()


@node(inputs=[name, pyproject], outputs=greeting)
def greet(name: str, settings: dict[str, Any]) -> str:
    language = settings.get("language", "en")
    if language == "en":
        return f"Hello, {name}"

    if language == "es":
        return f"Hola, {name}"

    raise ValueError("Language not supported")
```

```toml title="pyproject.toml"
[tool.my_tool]
language = "en"
```

The example above reads the `language` parameter from the `pyproject.toml` file and uses it to customize the greeting message.
The data is passed as a dictionary to the node.

For more information on the pyproject.toml format, see [writing your pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#writing-your-pyproject-toml).
