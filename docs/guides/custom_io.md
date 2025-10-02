# Creating a IO class

This guide will help you create a new IO class by extending the base classes provided in `ordeq.framework.io`.
IO classes are basic building block in `ordeq` to abstract IO operations from data transformations.

Frequently used IO implementations are offered out-of-the-box as `ordeq` packages.
For instance, there is support for JSON, YAML, Pandas, NumPy, Polars and many more.
These can be used where applicable and serve as reference implementation for new IO classes.

## Understanding the IO Base Class

The `IO` class is an abstract base class that defines the structure for loading and saving data.
It includes the following key methods:

- **`load()`**: Method to be implemented by subclasses for loading data.
- **`save(data)`**: Method to be implemented by subclasses for saving data.

## Example: FaissIndex

Before creating a custom IO class, first consider the following implementation using the Faiss library.
The `FaissIndex` class extends the `IO` class and implements the `load` and `save` methods:

```python
from dataclasses import dataclass
from pathlib import Path
import faiss
from ordeq.framework.io import IO


@dataclass(frozen=True, kw_only=True)
class FaissIndex(IO[faiss.Index]):
    path: Path

    def load(self) -> faiss.Index:
        return faiss.read_index(str(self.path))

    def save(self, index: faiss.Index) -> None:
        faiss.write_index(index, str(self.path))
```

## Creating Your Own IO Class

In this section, we will go step-by-step through the creation of a simple text-based file dataset.

### Define Your IO Class

Create a new class that extends the `IO` class and implement the `load` and `save` methods.

```python
from dataclasses import dataclass
from pathlib import Path
from ordeq.framework.io import IO


@dataclass(frozen=True, kw_only=True)
class CustomIO(IO):
    path: Path

    def load(self):
        pass

    def save(self, data):
        pass
```

### Implement the `load` Method

This method should contain the logic for loading your data.
For example:

```python
def load(self):
    return self.path.read_text()
```

### Implement the `save` Method

This method should contain the logic for saving your data.
For example:

```python
def save(self, data):
    self.path.write_text(data)
```

### Load- or save arguments

The `path` attribute is used by both the `load` and `save` method.
It's also possible to provide parameters to the individual methods.
For instance, we could let the user control the newline character used by `write_text`:

```python
from dataclasses import dataclass
from pathlib import Path
from ordeq.framework.io import IO


@dataclass(frozen=True, kw_only=True)
class CustomIO(IO):
    path: Path

    def load(self):
        return self.path.read_text()

    def save(self, data, newline: str = "\n"):
        self.path.write_text(data, newline=newline)
```

A common pattern when using third party functionality is to delegate keyword arguments to another function.

Below is an example of this for a Pandas CSV IO class:

```python
from dataclasses import dataclass
from pathlib import Path
import pandas as pd
from ordeq.framework.io import IO


@dataclass(frozen=True, kw_only=True)
class PandasCSV(IO[pd.DataFrame]):
    path: Path

    def load(self, **load_args) -> pd.DataFrame:
        return pd.read_csv(self.path, **load_args)

    def save(self, data: pd.DataFrame, **save_args):
        data.write_csv(self.path, **save_args)
```

### Providing type information

We can provide the `str` argument to `IO` to indicate that `CustomIO` class loads and saves strings.
This type should match the return type of the `load` method and the first parameter of the `save` method.

```python
from dataclasses import dataclass
from pathlib import Path
from ordeq.framework.io import IO


@dataclass(frozen=True, kw_only=True)
class CustomIO(IO[str]):  # IO operates on type `str`
    path: Path

    def load(self) -> str:  # and thus returns a `str` on load
        return self.path.read_text()

    def save(
        self, data: str
    ) -> None:  # and takes a `str` as first argument to `save`
        self.path.write_text(data)
```

### Read-only and write-only classes

While most data need to be loaded and saved alike, this is not always the case.
If in our code one of these operations is not necessary, then we can choose to not implement them.

Practical examples are:

- **Read-only**: When loading machine learning models from a third party registry where we have only read permissions (e.g. HuggingFace).
- **Write-only**: when a Matplotlib plot is rendered to a PNG file, we cannot load the `Figure` back from the PNG data.

#### Creating a Read-only class using `Input`

For a practical example of a class that is Read-only, we will consider generating of synthetic sensor data.
The `SensorDataGenerator` class will extend the `Input` class, meaning it will only have to implement the `load` method.

```python
import random
from dataclasses import dataclass
from typing import Any
from ordeq.framework.io import Input


@dataclass(frozen=True, kw_only=True)
class SensorDataGenerator(Input[dict[str, Any]]):
    """Example Input class to generate synthetic sensor data

    Example usage:

        >>> generator = SensorDataGenerator(sensor_id="sensor_3")
        >>> data = generator.load()
        {'sensor_id': 'sensor_3', 'temperature': 22.001252691230633, 'humidity': 35.2674852725557}
    """

    sensor_id: str

    def load(self) -> dict[str, Any]:
        """Simulate reading data from a sensor"""
        return {
            "sensor_id": self.sensor_id,
            "temperature": random.uniform(20.0, 30.0),
            "humidity": random.uniform(30.0, 50.0),
        }
```

Saving data using this dataset would raise a `ordeq.framework.io.IOException` explaining the save method is not implemented.

Similarly, you can inherit from the `Output` class for IO that only require to implement the `save` method.
The `ordeq-matplotlib` package contains an example of this in `MatplotlibFigure`.
