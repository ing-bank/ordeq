# Creating an IO class

This guide will help you create a new IO class by extending the base classes provided by Ordeq.
IO classes are basic building block in `ordeq` to abstract IO operations from data transformations.

Frequently used IO implementations are offered out-of-the-box as `ordeq` packages.
For instance, there is support for JSON, YAML, Pandas, NumPy, Polars and many more.
These can be used where applicable and serve as reference implementation for new IO classes.

## Creating your own IO class

In this section, we will go step-by-step through the creation of a simple text-based file dataset.
All IO classes implement the `IO` class.
The `IO` class is an abstract base class that defines the structure for loading and saving data.
It includes the following key methods:

- **`load()`**: Method to be implemented by subclasses for loading data.
- **`save(data)`**: Method to be implemented by subclasses for saving data.

First, create a new class that extends the `IO` class and implement these `load` and `save` methods.
The class should also have an `#!python __init__` method to initialize the necessary attributes, such as the file path.

!!! question "Which IO attributes should be in the `#!python __init__`?"

    Attributes that are necessary for __both loading and saving data__ should be defined in the `__init__` method.
    For example, a file path or database connection string.

```python
from pathlib import Path

from ordeq import IO


class CustomIO(IO):
    def __init__(self, path: Path):
        self.path = path
        super().__init__()

    def load(self):
        pass

    def save(self, data):
        pass
```

The `load` method should contain the logic for loading your data.
For example:

```python
def load(self):
    return self.path.read_text()
```

The `save` method should contain the logic for saving your data.
For example:

```python
def save(self, data):
    self.path.write_text(data)
```

!!!warning  "Save methods should not return anything"
    Save methods should always return `#!python None`.
    Ordeq will raise an error if a save method returns another type.

### Load- and save arguments

The `path` attribute is used by both the `load` and `save` method.
It's also possible to provide parameters to the individual methods.
For instance, we could let the user control the newline character used by `write_text`:

```python hl_lines="9"
class CustomIO(IO):
    def __init__(self, path: Path):
        self._path = path
        super().__init__()

    def load(self):
        return self._path.read_text()

    def save(self, data, newline: str = "\n"): # (1)!
        self._path.write_text(data, newline=newline)
```

1. The `newline` argument is specific to the `save` method.

All arguments to the load and save methods (except `#!python self` and `data`) should have a default value.

A common pattern when using third party functionality is to delegate keyword arguments to another function.
Below is an example of this for the `CustomIO` class:

```python hl_lines="6 7 9 10"
class CustomIO(IO):
    def __init__(self, path: Path):
        self._path = path
        super().__init__()

    def load(self, **load_options):
        return self._path.read_text(**load_options)

    def save(self, data, **save_options):
        self._path.write_text(data, **save_options)
```

The `CustomIO` class can now be used as follows:

```python
custom_io = CustomIO(path=Path("data.txt"))
data = custom_io.load(errors="ignore")
custom_io.save("Hello, world!", newline="\n")
```

## Tips & tricks

### Providing type information

We can provide the `#!python str` argument to `IO` to indicate that `CustomIO` class loads and saves strings.

```python hl_lines="1 6 9"
class CustomIO(IO[str]):  # (1)!
    def __init__(self, path: Path):
        self._path = path
        super().__init__()

    def load(self) -> str:  # (2)!
        return self._path.read_text()

    def save(self, data: str) -> None:  # (3)!
        self._path.write_text(data)
```

1. `#!python IO[str]` indicates that the IO operates on type `#!python str`
1. The `load` returns a `#!python str`
1. The `save` takes a `#!python str` as first argument

Ordeq will check that the signature of the `load` and `save` methods match the specified type.
For instance, the following implementation would raise a type error:

```python hl_lines="1 6 9"
class CustomIO(IO[str]):  # (1)!
    def __init__(self, path: Path):
        self.path = path
        super().__init__()

    def load(self) -> bool:  # (2)!
        return self.path.exists()

    def save(self, data: int) -> None:  # (3)!
        self.path.write_text(data)
```

1. `IO[str]` indicates that the IO operates on type `str`
1. This raises a type error: `load` should return `str`
1. This raises a type error: `save` should take `str`

Ordeq also supports static `load` and `save` methods.
In this case the `#!python self` argument is omitted.

### Using `dataclass` for IO classes

To simplify the definition of IO classes, you can use the `dataclass` decorator from the [dataclasses] library.
This allows us to define the attributes of the class in a more concise way.
Let's reconsider our running example using `#!python @dataclass`:

```python hl_lines="1 4"
from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class CustomIO(IO[str]):
    path: Path

    def load(self) -> str:
        return self.path.read_text()

    def save(self, data: str) -> None:
        self.path.write_text(data)
```

Using `#!python @dataclass` to define IO classes is optional and purely for convenience.
The load and save methods can be implemented as usual.
Please refer to the [dataclasses] documentation for more information.

### Stay close to the underlying API

In most cases, the IO class will be a thin adapter around an existing API or library.
When creating a new IO class, try to stay close to the underlying API to make it easier for users to understand and use your IO class:

- try to use the same parameter names and types as the underlying API.
- create one IO class per API or data format.

Here is an example that is **not recommended**:

```python hl_lines="4 7-9"
@dataclass(frozen=True)
class PandasCSVOrExcel(IO[pd.DataFrame]):
    path: Path
    is_excel: bool

    def load(self) -> pd.DataFrame:
        if self.is_excel:  # (1)!
            return pd.read_excel(self.path)
        return pd.read_csv(self.path)

    # (save omitted for brevity)
```

1. This is not recommended because, the `is_excel` parameter makes it unclear what the load method will do.

Instead, create two separate IO classes: `PandasCSV` and `PandasExcel`.
This makes it clearer what each class does and avoids confusion about the parameters.

## Read-only and write-only classes

While most data need to be loaded and saved alike, this is not always the case.
If in our code one of these operations is not necessary, then we can choose to not implement them.

Practical examples are:

- **Read-only**: when loading machine learning models from a third party registry where we have only read permissions (e.g. HuggingFace).
- **Write-only**: when a Matplotlib plot is rendered to a PNG file, we cannot load the `Figure` back from the PNG data.

### Creating a read-only class using `Input`

For a practical example of a class that is read-only, we will consider generating of synthetic sensor data.
The `SensorDataGenerator` class will extend the `Input` class, meaning it will only have to implement the `load` method.

````python hl_lines="3 7"
import random

from ordeq import Input


@dataclass(frozen=True, kw_only=True)
class SensorDataGenerator(Input[dict[str, Any]]): # (1)!
    """Example Input class to generate synthetic sensor data

    Example usage:

    ```pycon
    >>> generator = SensorDataGenerator(sensor_id="sensor_3")
    >>> data = generator.load()
    {'sensor_id': 'sensor_3', 'temp': 22.0..., 'humidity': 35.26...}
    ```

    """

    sensor_id: str

    def load(self) -> dict[str, Any]:
        """Simulate reading data from a sensor"""
        return {
            "sensor_id": self.sensor_id,
            "temperature": random.uniform(20.0, 30.0),
            "humidity": random.uniform(30.0, 50.0),
        }
````

1. `Input` indicates to Ordeq that this class is read-only.

Saving data using this dataset would raise a `ordeq.IOException` explaining the save method is not implemented.

Similarly, you can inherit from the `Output` class for IO that only require to implement the `save` method.
The `ordeq-matplotlib` package contains an example of this in `MatplotlibFigure`.

[api-docs]: ../api/ordeq_pandas.md
[dataclasses]: https://docs.python.org/3/library/dataclasses.html
