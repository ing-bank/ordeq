# Parametrizing IOs

A parameterized IO is an IO that uses a _parameter_ to configure its load or save behavior.
Typical examples of parameters are environment variables, command line arguments, or configuration files.
These parameters can configure various aspects of the IO, such as file paths and connection strings.

For example, you can parametrize an IO to:

- save a JSON file to a path based on a command line argument
- load an Excel sheet, where the sheet name is taken from a configuration file
- make an API request to a URL that is determined from an environment variable

### Approach

To create a parameter for an IO, we need:

- a custom IO class (see the guide on [custom IOs](custom_io.md))
- the parameter IO (the environment variable, command line argument, configuration file, etc.)

The approach is as follows:

- The custom IO class will take the parameter IO as an attribute
- The `load` and `save` methods load the parameter IO
- The `load` and `save` methods use the loaded parameter to load or save the data

## Examples

### Saving a file based on a command line argument

The following example shows how to load a JSON file based on a command line argument.
First, we create a custom class `JSONWithParameter`.

!!! info "Install `ordeq-args` and `ordeq-files`"

    To follow the example below, you need to install the `ordeq-args` and `ordeq-files` package.

```python title="json_with_parameter.py"
import json
from pathlib import Path
from functools import cached_property
from dataclasses import dataclass

from ordeq import Input, IO
from ordeq_args import CommandLineArg
from ordeq_files import JSON


@dataclass(frozen=True)
class JSONWithParameter(JSON):
    path_io: CommandLineArg[Path]

    @cached_property
    def path(self) -> Path:
        return self.path_io.load()
```

This IO inherits from the `JSON` IO in `ordeq-files`, but instead of taking a static `path` argument, it takes a
`path_io` argument, which is a `CommandLineArg` IO that loads a `Path`.
On load and save, the `path` property will return the path from the command line argument.

We can use the parametrized IO as follows:

```python title="main.py"
from ordeq import node, run
from ordeq_files import JSON, YAML
from ordeq_args import CommandLineArg
from pathlib import Path
from json_with_parameter import JSONWithParameter

source = YAML(path=Path("to/source.yaml"))
target = JSONWithParameter(path_io=CommandLineArg(name="--target", type=Path))


@node(inputs=source, outputs=target)
def convert_yaml_to_json(data: dict) -> dict:
    return data


if __name__ == "__main__":
    run(convert_yaml_to_json)
```

You can now run `main.py` from the command line, and specify the target path as argument:

```bash
python src/main.py --target output.json
```

This will copy the contents of `source.yaml` to `output.json`.

### Loading an Excel sheet based on a configuration file

The following example shows how to load an Excel sheet based on a configuration file.
In the example we will assume the configuration is stored in a YAML.

First, we create a custom class `PandasExcel`.
Note that this class resembles the `PandasExcel` offered in `ordeq-pandas`, but with a parameter IO `config`.

!!! info "Install `ordeq-files` and `pandas`"

    To follow the example below, you need to install the `ordeq-files` and `pandas` packages.

```python title="pandas_excel.py"
from ordeq import IO, Input
import pandas as pd
from pathlib import Path


class PandasExcel(Input[pd.DataFrame]):
    def __init__(self, path: Path, config: IO[dict]):
        self.path = path
        self.config = config
        super().__init__()

    def load(self) -> pd.DataFrame:
        config = self.config.load()  # e.g. {"sheet_name": "Sheet1"}
        return pd.read_excel(self.path, **config)
```

On load, the `PandasExcel` IO will load the configuration dictionary from the `config` IO, and pass the configuration as
keyword arguments to `pd.read_excel`.

We can initialize `PandasExcel` with any IO that loads a dictionary.
For example, we can use the `YAML` IO from `ordeq-files` as a parameter:

```pycon
>>> from pandas_excel import PandasExcel
>>> PandasExcel(
...     path=Path("data.xlsx"),
...     config=YAML(path=Path("config.yaml"))
... )
```

Suppose the configuration file `config.yaml` contains:

```yaml
sheet_name: Sheet8
```

When we do `xlsx.load()`, it will load the Excel file `data.xlsx` using the sheet name `Sheet8`.

Because the configuration is loaded from a file, we can change the configuration without changing the code.
For instance, we can easily add more configuration to the file, such as `header` and `usecols`:

```yaml
sheet_name: Sheet8
header: 0
usecols: A:C
```

New keys in the configuration file will be passed as keyword arguments to `pd.read_excel`.

!!! warning "Keep parameters simple"

    IOs are used to load and save data, and should not perform any transformations.
    If you find yourself applying transformations on load or save, consider creating a node instead.

### Make a request to an endpoint from an environment variable

Next, we will create an IO that makes a request to an endpoint, where the endpoint is created from an environment
variable.

!!! info "Install `ordeq-args` and `requests`"

    To follow the example below, you need to install the `ordeq-args` and `requests` package.

```python title="user_request.py"
from ordeq_args import EnvironmentVariable
from ordeq import IO
import requests


class UsersRequest(IO[requests.Response]):
    def __init__(self, idx: IO[str]):
        self.base_url = "https://jsonplaceholder.typicode.com/users/"
        self.idx = idx
        super().__init__()

    def load(self) -> requests.Response:
        idx = self.idx.load()
        url = f"{self.base_url}/{idx}"
        return requests.get(url)
```

This IO requests users from the [JSON placeholder API][json-placeholder-api].
You can also navigate to the URL in your browser to see the response.
The environment variable contains the user ID to request.

The `UsersRequest` IO can then be used as follows:

```pycon
>>> from user_request import UsersRequest
>>> from ordeq_args import EnvironmentVariable
>>> idx = EnvironmentVariable(name="USER_ID")
>>> response = UsersRequest(idx=idx)
>>> import os
>>> os.environ['USER_ID'] = '1'
>>> response.load()
b'{"id":1,"name":"Leanne Graham", ...}'
>>> os.environ['USER_ID'] = '2'
>>> response.load()
b'{"id":2,"name":"Ervin Howell", ...}'
>>> ...
```

Environment variables are typically used to configure sensitive information, like authentication details.
The example above extends to these types of parameters as well.

## Best practices

Parameters are a powerful way to make your IOs more flexible and reusable.
By composing an IO with a parameter IO, you can easily change the behavior of the IO without changing code.

When adding parameters to your IOs, consider the following best practices:

- **Keep parameters simple**:
    IOs should not perform any transformations.
    If the load or save logic is getting complex, consider creating a node instead.

- **Caching**:
    The approach above loads the parameter IO every time the `load` or `save` method is called.
    You can implement caching to avoid loading the parameter multiple times.

- **Manage reuse**
    If you find yourself reusing the same parameter IO across different IOs, consider creating a node instead.

!!! tip "Open a GitHub issue"

    If you have any questions or suggestions, feel free to [open an issue][new-issue] on GitHub!

## FAQ

#### Why do I have to create a custom class to parametrize an IO?

The IOs offer by Ordeq packages do not support parametrization out of the box.
We recommend custom IOs for parametrization, as this approach provides most flexibility.

#### What if I want to fall back to other parameters?

If you have multiple parameters providing you the same information, you can implement a fallback mechanism with a custom IO.
For instance, you can create a custom IO that first checks if a command line argument is provided, and if not, falls back to the environment variable.

[json-placeholder-api]: https://jsonplaceholder.typicode.com/users/
[new-issue]: https://github.com/ing-bank/ordeq/issues/new
