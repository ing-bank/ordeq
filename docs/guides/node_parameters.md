# Node parameters

Passing parameters to nodes is a powerful way to customize their behavior without modifying the node's code.
In Ordeq, parameters are just native IOs and need not be treated differently than regular inputs and outputs.

Commonly used parameter types that are supported out of the box include:

- Python built-in types: `str`, `int`, `float`, `bool`
- Configuration files (TOML, YAML, and JSON)
- Pydantic models or dataclass instances
- Command line arguments or environment variables

## Why use IOs for parameters?

Although it is possible to use plain variables in as parameters, it is not recommended.
Using IOs has several advantages:

- **Clarity**: It is clear which parameters a node depends on. The parameters are included in `run` and `viz` outputs.
- **Maintainability**: Configuration and transformations are separated, making it easier to change one without affecting the other. For example, we could easily change a parameter to be read from a configuration file or command line argument.
- **Reproducibility**: When the behavior of a node is fully determined by its inputs, this makes it easier to reproduce results and avoid unintended side effects. Moreover, this means Ordeq can avoid recomputation when the inputs have not changed.

Example using global variables (not recommended):

!!! warning "Avoid using global variables as parameters"

    The following example is a demonstration of what is not advised, and should be avoided in practice.
    For instance, the parameters will not appear in the `run` and `viz` outputs.

```python
from ordeq import IO, node

name_str = IO()
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
from ordeq import IO, Input, node

name_str = IO()
greeting = IO()
is_excited = Input[bool](False)


@node(inputs=[name_str, is_excited], outputs=greeting)
def greet(name: str, excited: bool) -> str:
    message = f"Hello, {name}"
    if excited:
        message += "!"
    return message
```

This way, the `greet` node is fully defined by its inputs and outputs, for instance making it possible to avoid recomputation when the inputs have not changed.

## Configuration files

This section shows several examples on how to read parameters from configuration files and pass them to nodes.

### Reading from a YAML or JSON

YAML and JSON are two popular formats for configuration due to their readability and support for complex data structures.
The following example shows how to read parameters from a YAML file and pass them to a node:

!!! note "Install the `ordeq-yaml` package to follow this example"

    The following example requires the `ordeq-yaml` package.
    Please install it if you want to follow along.

=== "pipeline.py"

    ```python
    from pathlib import Path

    from ordeq import IO, Input, node
    from ordeq_yaml import YAML

    name = Input("Alice")
    config = YAML(path=Path("config.yaml"))
    greeting = IO()


    @node(inputs=[name, config], outputs=greeting)
    def greet(name: str, cfg: dict) -> str:
        if cfg["language"] == "en":
            return f"Hello, {name}"
        if cfg["language"] == "es":
            return f"Hola, {name}"
        raise ValueError("Language not supported")
    ```

=== "config.yaml"

    ```yaml
    language: "en"
    ```

Likewise, here is the same example using JSON:

!!! note "Install the `ordeq-files` package to follow this example"

    The following example requires the `ordeq-files` package.
    Please install it if you want to follow along.

=== "pipeline.py"

    ```python
    from pathlib import Path

    from ordeq import IO, Input, node
    from ordeq_files import JSON

    name = Input("Alice")
    config = JSON(path=Path("config.json"))
    greeting = IO()


    @node(inputs=[name, config], outputs=greeting)
    def greet(name: str, cfg: dict) -> str:
        if cfg["language"] == "en":
            return f"Hello, {name}"
        if cfg["language"] == "es":
            return f"Hola, {name}"
        raise ValueError("Language not supported")
    ```

=== "config.json"

    ```json
    {"language": "en"}
    ```

The examples above reads the `language` parameter from the configuration file and uses it to customize the greeting message.

### Reading from a `pyproject.toml`

The pyproject.toml format is the standard way to configure Python projects.
The [`[tool]`](https://packaging.python.org/en/latest/specifications/pyproject-toml/#pyproject-tool-table) table is intended for tool-specific configuration.
Ordeq can read parameters from a `[tool.your_tool_name]` section in `pyproject.toml` and pass it to one or more nodes using little code.

!!! note "Install the `ordeq-pyproject` package to follow this example"

    The following example requires the `ordeq-pyproject` package.
    Please install it if you want to follow along.

=== "pipeline.py"

    ```python
    from pathlib import Path

    from ordeq import IO, Input, node
    from ordeq_pyproject import Pyproject

    name = Input("Alice")
    language = Pyproject(
        path=Path("pyproject.toml"), section="tool.my_tool.language"
    )
    greeting = IO()


    @node(inputs=[name, language], outputs=greeting)
    def greet(name: str, language: str) -> str:
        if language == "en":
            return f"Hello, {name}"
        if language == "es":
            return f"Hola, {name}"

        raise ValueError("Language not supported")
    ```

=== "pyproject.toml"

    ```toml title="pyproject.toml"
    [tool.my_tool]
    language = "en"
    ```

The example above reads the `language` parameter from the `pyproject.toml` file and uses it to customize the greeting message.
The data is passed as a dictionary to the node.

For more information on the pyproject.toml format, see [writing your pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#writing-your-pyproject-toml).

## Structured configuration

When reading parameters from configuration files, it is often useful to validate the data to ensure it meets certain criteria.
Ordeq provides built-in support for structured configuration using dataclasses or Pydantic models.
These represent configuration as a structured object.
This allows for input validation, type checking, and autocompletion in IDEs.

### Using dataclasses

[Dataclasses] are a simple way to define structured parameters with validation.
The following example shows a dataclass that is read from a YAML file, validated and passed to a node:

!!! note "Install the `ordeq-common` and `ordeq-yaml` packages to follow this example"

    The following example requires the `ordeq-common` and `ordeq-yaml` packages.
    Please install these if you want to follow along.

=== "pipeline.py"

    ```python
    from dataclasses import dataclass
    from pathlib import Path

    from ordeq import IO, Input, node
    from ordeq_common import Dataclass
    from ordeq_yaml import YAML


    @dataclass
    class GreetingConfig:
        language: str = "en"
        excited: bool = False


    name = Input("Alice")
    config = Dataclass(io=YAML(path=Path("config.yml")), dataclass=GreetingConfig)
    greeting = IO()


    @node(inputs=[name, config], outputs=greeting)
    def greet(name: str, cfg: GreetingConfig) -> str:
        if cfg.language == "en":
            return f"Hello, {name}"
        if cfg.language == "es":
            return f"Hola, {name}"

        raise ValueError("Language not supported")
    ```

=== "config.yaml"

    ```yaml
    language: "en"
    excited: true
    ```

### Using Pydantic models

Pydantic models are another great way to define structured parameters with validation.
The following example a Pydantic model that is read from a YAML file, validated and passed to a node:

!!! note "Install the `ordeq-pydantic` and `ordeq-yaml` packages to follow this example."

    The following example requires the `ordeq-pydantic` and `ordeq-yaml` packages.
    Please install them if you want to follow along.

=== "pipeline.py"

    ```python
    from pathlib import Path

    from ordeq import IO, Input, node
    from ordeq_pydantic import PydanticModel
    from ordeq_yaml import YAML
    from pydantic import BaseModel


    class GreetingConfig(BaseModel):
        language: str = "en"
        excited: bool = False


    name = Input("Alice")
    config = PydanticModel(
        io=YAML(path=Path("config.yml")), model_type=GreetingConfig
    )
    greeting = IO()


    @node(inputs=[name, config], outputs=greeting)
    def greet(name: str, cfg: GreetingConfig) -> str:
        if cfg.language == "en":
            return f"Hello, {name}"
        if cfg.language == "es":
            return f"Hola, {name}"

        raise ValueError("Language not supported")
    ```

=== "config.yaml"

    ```yaml
    language: "en"
    excited: true
    ```

=== "config-invalid.yaml"

    ```yaml
    language: 123  #(1)!
    excited: "yes"  #(2)!
    ```

    1. Invalid type, should be `#!python str`
    1. Invalid type, should be `#!python bool`

When `config-invalid.yaml` is used, Pydantic will raise a validation error before the `greet` node is called.
Pydantic provides detailed error messages that help identify which fields are invalid and why:

```python-traceback
ordeq._io.IOException: Failed to load ...
language
  Input should be a valid string [type=string_type, input_value=123, input_type=int]
    For further information visit https://errors.pydantic.dev/...
```

## Command line arguments and environment variables

Ordeq can also read parameters from command line arguments or environment variables using the `ordeq-args` package.
This is particularly useful if you want to customize the behavior of a pipeline without modifying the code or configuration files.
Here are examples of both approaches:

!!! note "Install the `ordeq-args` package to follow this example"

    The following example requires the `ordeq-args` package.
    Please install it if you want to follow along.

=== "pipeline.py (Command line argument)"

    ```python
    from ordeq import IO, Input, node
    from ordeq_args import CommandLineArg

    name = Input("Alice")
    language = CommandLineArg[str](name="--language", default="en")
    greeting = IO()


    @node(inputs=[name, language], outputs=greeting)
    def greet(name: str, language: str) -> str:
        if language == "en":
            return f"Hello, {name}"
        if language == "es":
            return f"Hola, {name}"
        raise ValueError("Language not supported")
    ```

=== "pipeline.py (Environment variable)"

    ```python
    from ordeq import IO, Input, node
    from ordeq_args import EnvironmentVariable

    name = Input("Alice")
    language = EnvironmentVariable[str](name="LANGUAGE", default="en")
    greeting = IO()


    @node(inputs=[name, language], outputs=greeting)
    def greet(name: str, language: str) -> str:
        if language == "en":
            return f"Hello, {name}"
        if language == "es":
            return f"Hola, {name}"
        raise ValueError("Language not supported")
    ```

In this example, the `language` parameter is read from a command-line argument `--language`.
You can run the pipeline with different languages like this:

```bash
python pipeline.py --language es
```

This will produce the greeting in Spanish: `Hola, Alice`.

Alternatively, you can read the parameter from an environment variable by using the `EnvironmentVariable` IO instead of `CommandLineArg`.
Set the environment variable and run the pipeline like this:

```bash
export LANGUAGE=es
python pipeline.py
```

### Parsing to specific types

You can parse a command line argument to a specific type using a custom parser function.
For example, to parse a date string to a `date` object, you can use the `date.fromisoformat` method:

!!! tip "Check out the `argparse` documentation"

    For more information on custom type parsing, see the [argparse documentation][argparse].

=== "pipeline.py"

    ```python
    from datetime import date

    from ordeq import node
    from ordeq_args import CommandLineArg

    date_arg = CommandLineArg[date]("--date", type=date.fromisoformat)


    @node(inputs=date_arg)
    def show_date(dt: date) -> str:
        return f"Today's date is {date}"
    ```

When running the pipeline, you can pass the date in ISO format:

```shell
python pipeline.py --date 2024-06-15
```

Which will output: `Today's date is 2024-06-15`.
This is useful for embedding time logic into your pipeline, such as incremental processing of data based on dates.

[argparse]: https://docs.python.org/3/library/argparse.html#type
[dataclasses]: https://docs.python.org/3/library/dataclasses.html
