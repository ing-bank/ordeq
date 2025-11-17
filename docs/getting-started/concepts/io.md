# IO

IO refers to the loading and saving of data.
For example, you might have an IO that loads a CSV file.
In Ordeq, an IO is represented by an `IO` class.

## Why use IOs?

To understand why IOs are useful, let's look at a simple example.
Suppose we want to load a simple CSV file.
We could write a function that loads the CSV file directly:

```python
import csv
from pathlib import Path


def load_csv(path: Path) -> list[list[str]]:
    with path.open(mode="r") as f:
        reader = csv.reader(f)
        return list(reader)
```

The main downside of this approach is that it immediately loads the data when the IO details, like the path to the file, are defined:

```pycon
>>> load_csv(Path("to/data.csv"))
[(1, "kiwis", 7.2), (2, "grapefruits", 1.4)]
```

Instead, we can use the `CSV` IO from `ordeq_files` to represent the CSV file:

```python
from pathlib import Path

from ordeq_files import CSV

io = CSV(path=Path("to/data.csv"))
```

Defining the IO does not load the data yet, until we tell it to:

```pycon
>>> io.load()
[(1, "kiwis", 7.2), (2, "grapefruits", 1.4)]
```

!!! note "IOs do not hold any data"

    IOs do not hold any data themselves, they just know how to load and save data.

This means IOs can be defined separately from when they are used.
It also means IOs can be easily reused in different places.

The same IO can be used to save data as well:

```pycon
>>> data_to_save = [(1, "apples", 3.5), (2, "bananas", 4.0)]
>>> io.save(data_to_save)
```

!!! note "The `data` argument"

    The first argument to the `save` method, which is the data to be saved, is positional-only.
    This is to avoid ambiguity, as it ensures the required data argument precedes any save options.

Lastly, IOs serve as convenient and lightweight representations of data in your project:

```pycon
>>> print(io)
CSV(path=PosixPath('to/data.csv'))
```

!!! info "More complex IOs"

    A key feature of IOs is that they abstract the loading and saving behaviour from the user.
    IOs are typically used to handle the interaction with file systems, cloud storage, APIs, databases and other data sources.
    Unlike the example above, these more complex IOs manage everything from authentication to (de)serialization.

Ordeq offers many off-the-shelf IOs for common data formats, such as CSV, Excel, JSON, Parquet, and SQL databases.
Refer to the [API documentation][api] for a full list of available IOs.

## Using IOs

IOs can be used stand-alone, for instance when exploring data in a Jupyter notebook.
Suppose you just received an Excel file from a colleague and want to take a look at it.
You can use the `PandasExcel` IO from `ordeq_pandas` to load and inspect the data:

```pycon
>>> from ordeq_pandas import PandasExcel
>>> from pathlib import Path
>>> fruit_sales = PandasExcel(path=Path("fruit_sales.xlsx"))
>>> df = fruit_sales.load()
>>> df.head(2)
Fruit       Quantity (kg)  Price   Store
0   apples          '3.5'   1.2     A
1  bananas          '4.0'   0.8     B
>>> df.dtypes
Fruit           object
Quantity (kg)   object
Price           float64
Store           object
dtype: object
```

Unfortunately the data types are not quite right.
We want to convert the `Quantity (kg)` column to `float` and rename the columns to be more convenient.
Furthermore, we want to drop the `Store` column as we don't need it.

### Load & save options

You can alter the loading behaviour of an IO through its _load options_:

```pycon
>>> fruit_sales = fruit_sales.with_load_options(
...     dtype={"Quantity (kg)": float},
...     usecols="A:C",
...     names=["fruit", "quantity_kg", "price"],
... )
>>> df = fruit_sales.load()
>>> df.dtypes
fruit           object
quantity_kg     float64
price           float64
dtype: object
```

Here, the load options are used to specify the data types, select specific columns, and rename a column.
Under the hood, these options are passed to `pandas.read_excel`.

!!! note "Building IO load and save options"

    The `with_load_options` and `with_save_options` methods return a new IO instance with the updated options.
    The original IO instance remains unchanged.

Similarly, you can alter the saving behaviour of an IO through its _save options_:

```pycon
>>> fruit_sales = fruit_sales.with_save_options(index=False)
>>> fruit_sales.save(df)
```

For more information on the available load and save options, refer to the documentation of the specific IO you are using.

!!! warning "IOs should not apply transformations"

    IOs should only be concerned with loading and saving data.
    Therefore, IOs should not apply any transformation on load or save.
    Some load or save options do incur what can be considered a _transformation_, like the casting or renaming done above.
    As a rule of thumb:

    - if the option is specific to your use case, it should be done outside the IO
    - if the option refers to an operation that is likely to be useful to others, it might be appropriate as a load/save option.
    - if the option is closely tied to the IO implementation, it is likely appropriate as a load/save option.

### Attributes

Often it can be useful to annotate IOs with additional metadata.
This metadata is stored as _attributes_ on the IO instance.
Examples of useful attributes include:

- the description (e.g., "Sales data by month")
- the layer of the data (e.g., raw, processed, final)
- the source of the data (e.g., internal, external, third-party)
- the owner of the data (e.g., team or person responsible)

Attributes can be assigned using the `with_attributes` method:

```python
from pathlib import Path

from ordeq_files import CSV

sales = CSV(path=Path("sales.csv")).with_attributes(
    description="Sales data by month",
    layer="gold",
    source="internal",
    owner="dwh-team@company.com",
)
```

Framework extensions like `ordeq-viz` can leverage these attributes to provide additional functionality.

!!! success "Where to go from here?"

    - See how IOs are used in [nodes]
    - Find out how to organise IOs with [catalogs]
    - See how to extend inject custom logic with [IO hooks][hooks]
    - Check out the [guide on creating custom IOs][custom-ios]

[api]: ../../api/ordeq/types.md
[catalogs]: ./catalogs.md
[custom-ios]: ../../guides/custom_io.md
[hooks]: hooks.md
[nodes]: nodes.md
