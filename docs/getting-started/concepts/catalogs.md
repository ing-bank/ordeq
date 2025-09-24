# Catalogs

A **catalog** is collection of IOs.
From experience, we find that separating these IO from transformations (nodes) keeps your code clean and maintainable.
Catalogs help you organize and swap IOs across different environments — such as local development, production, or testing — without changing your nodes.
This makes it easy to run the same pipeline with different data sources or destinations.

## Defining catalogs

To create a catalog, make a Python module where each IO is a variable. For example, a local catalog might look like this:

```python title="catalogs/local.py"
from ordeq_spark import SparkCSV

iris = SparkCSV(path="path/to/local/iris.csv")
predictions = SparkCSV(path="path/to/local/predictions.csv")
```

Here, `iris` and `predictions` are IOs pointing to local CSV files.

!!!info "IO naming convention"
    Following [PEP-8](https://peps.python.org/pep-0008/#function-and-variable-names), IO instances should be lowercased.
    For instance, use `iris` instead of `Iris`.
    IO classes, on the other hand, should be in `PascalCase`, such as `SparkCSV`.

For production, you might want to use different IOs, such as tables in a data lake:

```python title="catalogs/production.py"
from ordeq_spark import SparkIcebergTable

iris = SparkIcebergTable(table="iris")
predictions = SparkIcebergTable(table="predictions")
```

Notice that both catalogs use the same variable names (`iris`, `predictions`), but the IOs themselves are different:
one uses CSV files, the other uses Iceberg tables.

Now you can use the IOs in your nodes by importing the catalog:

```python title="nodes.py"
from ordeq import node
from pyspark.sql import DataFrame

from catalogs import local  # or 'production'

@node(
    inputs=local.iris,
    outputs=local.predictions,
)
def predict(iris: DataFrame) -> DataFrame:
    # Your prediction logic here
    ...

```

!!!tip "Avoid individual IO imports"
    It is best practice to import the catalog entirely, rather than individual IOs.
    This keeps the import statements clean, and makes it easier to switch catalogs.
    It also avoids name clashes between IOs and function arguments in your code.

## Switching between catalogs

You can select which catalog to use based on the environment that your code runs in.
An easy way to do this is by using an environment variable.
Say you want to switch between the local and production catalogs based on an environment variable called `ENV`.
You can do so as follows:

```python title="catalogs/__init__.py"
import os
from catalogs import local, production

catalog = local if os.getenv("ENV") == "local" else production
```

Now, you can use the resolved catalog in your nodes:

```python title="nodes.py"
from ordeq import node
from pyspark.sql import DataFrame

from catalogs import catalog  # resolves to 'local' or 'production'

@node(
    inputs=catalog.iris,
    outputs=catalog.predictions,
)
def predict(iris: DataFrame) -> DataFrame:
    # Your prediction logic here
    ...

```

When the environment variable `ENV=local` it uses the local catalog.
For any other value, it uses the production catalog.

## Ensuring consistency

It is important that all your catalogs define the same IOs (that is, the same variable names).
This prevents errors when switching between environments.

You can check catalog consistency using the `check_catalogs_are_consistent` function.
Here is how you would adapt the previous script:

```python title="catalogs/__init__.py"  hl_lines="2 6"
import os
from ordeq.framework.catalog import check_catalogs_are_consistent

from catalogs import local, production

check_catalogs_are_consistent(local, production)
catalog = local if os.getenv("ENV") == "local" else production
```

If the catalogs have different variable names, this function will raise an error, helping you catch mistakes early.

!!!tip "When (not) to use catalogs"
    Creating separate modules for different environments makes most sense if each module contains a different set of IOs that cannot be otherwise resolved at run-time.

    For instance, if the only difference between your local and production environments is the namespace, you can use environment variables or configuration file to set the table names dynamically, rather than creating separate catalogs:

    ```python title="catalog.py"
    from ordeq_spark import SparkCSV

    ns = os.getenv("NAMESPACE", "default")
    iris = SparkIcebergTable(table=f"{ns}.iris")
    predictions = SparkIcebergTable(table=f"{ns}.predictions")
    ```

    This approach is simpler and avoids the overhaead of multiple catalog modules.

## Extending catalogs
Often we do not want to create a new catalog from scratch, but rather extend an existing one.
For example, you might want to create a `staging` catalog that is similar to `production`, but with a few differences.
You can do this by importing the base catalog and overriding specific IOs:

```python title="catalogs/staging.py" hl_lines="5"
from ordeq_spark import SparkCSV

from catalogs.production import *

iris = SparkCSV(path="path/to/staging/iris.csv")  # Override iris IO
```

This way, the `staging` catalog inherits all IOs from `production`, except for `iris`, which is replaced with a CSV.

You can also extend catalogs, as follows:

```python title="catalogs/staging.py"  hl_lines="5"
from ordeq_spark import SparkCSV

from catalogs.production import *

iris_large = SparkCSV(path="path/to/staging/iris_large.csv")  # Extends with a new IO
```

Note that the extended catalog is not consistent with the `production` catalog, since it defines a new IO.

## Using catalogs in tests

Catalogs are useful for testing, because you can easily swap to test IOs.
First, define a test catalog with test IOs:

```python
from ordeq_spark import SparkCSV

iris = SparkCSV(path="path/to/test/iris.csv")
predictions = SparkCSV(path="path/to/test/predictions.csv")
```

You can place the catalog in the source package, with the other catalogs.
In that case, you can import it in your nodes as shown above.

If you place the catalog in another package, say the `tests` package, the easiest way to use the test catalog is to patch:

```python title="test_nodes.py"
from ordeq import run
from unittest import patch

import nodes
import tests

@patch("nodes.catalog", new=tests.catalog)
def test_it_predicts(catalog):
    actual = run(predict)
    assert predictions.load() == ...  # do your assertions here
```

!!!warning "Limitation"
    Patching a catalog only works if the catalog is a plain module, not a package.

If you do not want to create a new catalog, you can run nodes with alternative IOs directly:

```python title="test_nodes.py"
from ordeq import run
from ordeq_spark import SparkCSV

from catalogs import catalog

def test_it_predicts():
    actual = run(
        predict,
        io={catalog.iris: SparkCSV(path="path/to/test.csv")}
    )
    assert catalog.predictions.load() == ...  # do your assertions here
```

This is especially useful for unit tests.
Checkout the [node testing guide][node-testing] for more details.

[node-testing]: ../../guides/testing_nodes.md
