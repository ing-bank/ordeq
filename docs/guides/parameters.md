# Parameters

A parameter is an IO that is used by another IO to configure its load or save behavior.
Typical examples of parameters are environment variables, command line arguments, or configuration files.
These parameters can configure various aspects of the IO, such as file paths and connection strings.
For example, you might want to:

- save a JSON file to a path based on a command line argument
- load an Excel sheet, and the sheet name is taken from a configuration file
- make an API request, and the authentication is taken from an environment variable

### Approach

To create a parameter for an IO, we need two things:

- a custom IO class (see the guide on [custom IOs](custom_io.md))
- the parameter IO (the environment variable, command line argument, configuration file, etc.)

The approach is as follows:

- The custom IO class will take the parameter IO as an attribute
- The `load` and `save` methods load the parameter IO
- The `load` and `save` methods use the loaded parameter to load or save the data.

## Examples

### Saving a file based on a command line argument

The following example shows how to load a JSON file based on a command line argument.
First, we create a custom class `ParameterizedJSON`.

!!!info "Install `ordeq-args` and `ordeq-files`"
    To follow the example below, you need to install the `ordeq-args` and `ordeq-files` package.

```python
import json
from pathlib import Path
from functools import cached_property

from ordeq import Input, IO
from ordeq_args import CommandLineArg

class JSONWithParameter(IO[dict]):
    path: CommandLineArg[Path]

    @cached_property
    def _path(self) -> Path:
        return self.path.load()

    def load(self):
        with self._path.open(mode='r') as file:
            return json.load(file)

    def save(self, data: dict) -> None:
        with self._path.open(mode='w') as file:
            return json.dump(data, file)
```

The `ParameterizedJSON` IO takes a command line argument as a parameter.
Suppose we use the IO as follows:

```python title="main.py"
from ordeq import node
from ordeq_files import JSON
from ordeq_args import CommandLineArg
from pathlib import Path

source = JSON(path=Path('to/source.json'))
target = JSONWithParameter(path=CommandLineArg(name='--target', type=Path))

@node(inputs=source, outputs=target)
def copy_json(data: dict) -> dict:
    return data
```

Now you can run the node from the command line, and specify the target path as argument:

```bash
ordeq run --nodes main:copy_json --target output.json
```

This will copy the contents of `source.json` to `output.json`.

### Loading an Excel sheet based on a configuration file

The following example shows how to load an Excel sheet based on a configuration file.
In the example we will assume the configuration is stored in a YAML.

First, we create a custom class `PandasExcel`.
Note that this class resembles the `PandasExcel` offered in `ordeq-pandas`, but with a parameter IO `config`.

!!!info "Install `ordeq-files` and `pandas`"
    To follow the example below, you need to install the `ordeq-files` and `pandas` packages.

```python
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

On load, the `PandasExcel` IO will load the configuration dictionary from the `config` IO, and pass the configuration as keyword arguments to `pd.read_excel`.

We can initialize `PandasExcel` with any IO that loads a dictionary.
For example, we can use the `YAML` IO from `ordeq-files` as a parameter:

```python
xlsx = PandasExcel(
    path=Path("data.xlsx"),
    config=YAML(path=Path("config.yaml"))
)
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

!!!warning "Keep parameters simple"
    IOs are used to load and save data, and should not perform any transformations.
    If you find yourself applying transformations on load or save, consider creating a node instead.

### Make a request to an endpoint from an environment variable

Next, we will create an IO that makes a request to an endpoint, where the endpoint is created from an environment variable.

!!!info "Install `ordeq-args` and `requests`"
    To follow the example below, you need to install the `ordeq-args` and `requests` package.

```python
from ordeq_args import EnvironmentVariable
from ordeq import IO
import requests

class UsersRequest(IO[requests.Response]):
    def __init__(self, idx: IO[str]):
        self.base_url = 'https://jsonplaceholder.typicode.com/users/'
        self.idx = idx
        super().__init__()

    def load(self) -> requests.Response:
        idx = self.idx.load()
        url = f'{self.base_url}/{idx}'
        return requests.get(url)
```

This IO requests users from the [JSON placeholder API][json-placeholder-api].
You can also navigate to the URL in your browser to see the response.
The environment variable contains the user ID to request.

The `UsersRequest` IO can then be used as follows:

```pycon
>>> idx = EnvironmentVariable(name="USER_ID")
>>> response = Request(idx=idx)
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

If you have any questions or suggestions, feel free to [open an issue][new-issue] on GitHub!

[json-placeholder-api]: https://jsonplaceholder.typicode.com/users/

[new-issue]: https://github.com/ing-bank/ordeq/issues/new
