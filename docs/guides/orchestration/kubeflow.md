# Kubeflow integration

Ordeq allows you to define your data processing pipelines independently of the orchestration tool.
This separation of concerns leads to more modular, reusable, and testable code, making it easier to maintain and evolve your data processing workflows over time.
This guide demonstrates how to use Ordeq to define a machine learning pipeline and then orchestrate it using Kubeflow.

!!! info "Example code"

    The complete example code for this guide is available in the [Ordeq GitHub repository](https://github.com/ing-bank/ordeq/tree/main/examples/orchestration-kubeflow).

We will first recreate this example pipeline using Ordeq. Next, we will show how to orchestrate that pipeline using Kubeflow

## The ML pipeline

We base our example on a simple machine learning pipeline that trains a K-Nearest Neighbors (KNN) classifier on the Iris dataset.
The example is available in the [Kubeflow Pipelines documentation](https://www.kubeflow.org/docs/components/pipelines/user-guides/core-functions/build-advanced-pipeline/).
The pipeline consists of the following steps:

- `create_dataset`: Downloads the Iris dataset from a remote URL and saves it as a local CSV file.
- `normalize_dataset`: Normalizes the dataset using either Min-Max scaling or Standard scaling.
- `train_model`: Trains a KNN classifier on the normalized dataset and saves the trained model as a pickle file.

## Creating the Ordeq pipeline

Now that the code is written using Ordeq, we can focus on the domain logic without worrying about the orchestration details.

- `create_dataset`: With Ordeq, the copying of the CSV from remote to local comes nearly for free. This step is reduced to setting up the `ordeq_pandas.PandasCSV` IOs and defining the node.

```python title="ml_pipeline/preprocessing.py"
from my_pipeline import catalog


@node(inputs=catalog.csv_remote, outputs=catalog.csv_local)
def create_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Copies the remote iris dataset to a local CSV file."""
    return df
```

```python title="ml_pipeline/catalog.py"
csv_remote = PandasCSV(
    path="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
).with_load_options(
    names=[
        "Sepal_Length",
        "Sepal_Width",
        "Petal_Length",
        "Petal_Width",
        "Labels",
    ]
)
csv_local = PandasCSV(path="iris_dataset.csv")
```

- `normalize_dataset`: Now that Ordeq handles the IOs, we observe that the `standard_scaler` and `min_max_scaler` boolean flags could be simplified to a single `scaler` parameter that takes a string value. This makes the node definition cleaner and easier to understand.

```python title="ml_pipeline/preprocessing.py"
from my_pipeline import catalog


@node(
    inputs=[catalog.csv_local, catalog.scaler], outputs=catalog.csv_normalized
)
def normalize_dataset(
    df: pd.DataFrame, scaler: Literal["min_max", "standard"] | None = None
):
    labels = df.pop("Labels")

    match scaler:
        case "standard":
            scaler = StandardScaler()
        case "min_max":
            scaler = MinMaxScaler()
        case _:
            raise ValueError("Scaler must be either 'standard' or 'min_max'")

    df = pd.DataFrame(scaler.fit_transform(df))
    df["Labels"] = labels
    return df
```

```python title="ml_pipeline/catalog.py"
csv_normalized = PandasCSV(path="normalized_iris_dataset.csv")
scaler = Input[str]("standard")
```

- `train_model`: Similarly, the model training node is simplified by removing the IO handling code, allowing us to focus solely on the model training logic.
    For example, the random state that was hardcoded before is now passed as a parameter to the node, making sure that the code is reproducible when needed, but splits randomly by default.
    This is a key example where orchestration-specific code may interfere with the domain logic, in this case soundness of the ML model training.

```python title="ml_pipeline/train.py"
@node(
    inputs=[catalog.csv_normalized, catalog.n_neighbors, catalog.seed],
    outputs=catalog.knn_model,
)
def train_model(
    df: pd.DataFrame, n_neighbors: int, seed: int | None = None
) -> BaseEstimator:
    y = df.pop("Labels")
    X = df

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, random_state=seed
    )

    clf = KNeighborsClassifier(n_neighbors=n_neighbors)
    clf.fit(X_train, y_train)
    return clf
```

```python title="ml_pipeline/catalog.py"
knn_model = Pickle(path=Path("knn_model.pkl"))
n_neighbors = Input[int](3)
seed = Input[int | None](0)
```

## Running the pipeline locally

With the pipeline defined using Ordeq, we can now run it locally.
With Ordeq, this is as simple as calling the `run` function with the final node and the desired parameters.

```python title="run_local.py"
from ordeq import run

import ml_pipeline

run(ml_pipeline)
```

Apart from the readability and maintainability improvements in the pipeline code, we also get a nice visualization of the pipeline structure when running it locally:

```mermaid
graph TB
	subgraph legend["Legend"]
		direction LR
		node_type@{shape: rounded, label: "Node"}
		io_type_0@{shape: rect, label: "Input"}
		io_type_1@{shape: rect, label: "PandasCSV"}
		io_type_2@{shape: rect, label: "Pickle"}
	end

	subgraph pipeline["Pipeline"]
		direction TB
		ml_pipeline.catalog:csv_remote --> ml_pipeline.preprocessing:create_dataset
		ml_pipeline.preprocessing:create_dataset --> ml_pipeline.catalog:csv_local
		ml_pipeline.catalog:csv_local --> ml_pipeline.preprocessing:normalize_dataset
		ml_pipeline.catalog:scaler --> ml_pipeline.preprocessing:normalize_dataset
		ml_pipeline.preprocessing:normalize_dataset --> ml_pipeline.catalog:csv_normalized
		ml_pipeline.catalog:csv_normalized --> ml_pipeline.train:train_model
		ml_pipeline.catalog:n_neighbors --> ml_pipeline.train:train_model
		ml_pipeline.catalog:seed --> ml_pipeline.train:train_model
		ml_pipeline.train:train_model --> ml_pipeline.catalog:knn_model

		ml_pipeline.preprocessing:create_dataset@{shape: rounded, label: "create_dataset"}
		ml_pipeline.preprocessing:normalize_dataset@{shape: rounded, label: "normalize_dataset"}
		ml_pipeline.catalog:csv_local@{shape: rect, label: "csv_local"}
		ml_pipeline.train:train_model@{shape: rounded, label: "train_model"}
		ml_pipeline.catalog:csv_normalized@{shape: rect, label: "csv_normalized"}
		ml_pipeline.catalog:csv_remote@{shape: rect, label: "csv_remote"}
		ml_pipeline.catalog:knn_model@{shape: rect, label: "knn_model"}
		ml_pipeline.catalog:n_neighbors@{shape: rect, label: "n_neighbors"}
		ml_pipeline.catalog:scaler@{shape: rect, label: "scaler"}
		ml_pipeline.catalog:seed@{shape: rect, label: "seed"}
	end

	class node_type,ml_pipeline.preprocessing:create_dataset,ml_pipeline.preprocessing:normalize_dataset,ml_pipeline.train:train_model node
	class io_type_0,ml_pipeline.catalog:n_neighbors,ml_pipeline.catalog:scaler,ml_pipeline.catalog:seed io0
	class io_type_1,ml_pipeline.catalog:csv_local,ml_pipeline.catalog:csv_normalized,ml_pipeline.catalog:csv_remote io1
	class io_type_2,ml_pipeline.catalog:knn_model io2
	classDef node fill:#008AD7,color:#FFF
	classDef io fill:#FFD43B
	classDef io0 fill:#66c2a5
	classDef io1 fill:#fc8d62
	classDef io2 fill:#8da0cb

        style pipeline fill:transparent
```

## Running the pipeline with Kubeflow

The final step is to orchestrate the pipeline using Kubeflow.
Without loss of Kubeflow-specific functionality, such as "Output" or "Dataset" types, we can define the Kubeflow pipeline by wrapping the Ordeq nodes in Kubeflow components.

!!! info "More roads lead to Rome"

    There are many ways to map Ordeq nodes to Kubeflow components.
    This is just one example of how it can be done.
    The key point is that the core logic of the nodes remains unchanged, and only the orchestration-specific code is added around it.

For example, we can define the Kubeflow components as follows:

```python title="run_kubeflow.py"
from dataclasses import replace

from kfp import client
from kfp import dsl

from ordeq import run

from ml_pipeline import train, preprocessing, catalog


@dsl.component(packages_to_install=["pandas==1.3.5"])
def create_dataset(iris_dataset: dsl.Output[dsl.Dataset]):
    run(
        preprocessing.create_dataset,
        io={
            catalog.csv_local: replace(catalog.csv_local, path=iris_dataset.path)
        }
    )


@dsl.component(packages_to_install=["pandas==1.3.5", "scikit-learn==1.0.2"])
def normalize_dataset(
    input_iris_dataset: dsl.Input[dsl.Dataset],
    normalized_iris_dataset: dsl.Output[dsl.Dataset],
    scaler: str,
):
    run(
        preprocessing.normalize_dataset,
        io={
            catalog.csv_local: replace(catalog.csv_local, path=input_iris_dataset.path),
            catalog.csv_normalized: replace(catalog.csv_normalized, path=normalized_iris_dataset.path),
            catalog.scaler: scaler,
        },
    )


@dsl.component(packages_to_install=["pandas==1.3.5", "scikit-learn==1.0.2"])
def train_model(
    normalized_iris_dataset: dsl.Input[dsl.Dataset],
    model: dsl.Output[dsl.Model],
    n_neighbors: int,
):
    run(
        train.train_model,
        io={
            catalog.csv_normalized: replace(catalog.csv_normalized, path=normalized_iris_dataset.path),
            catalog.knn_model: replace(catalog.knn_model, path=model.path),
            catalog.n_neighbors: n_neighbors,
        },
    )


@dsl.pipeline(name="iris-training-pipeline")
def my_pipeline(scaler: str, neighbors: list[int], seed: int | None = 0):
    create_dataset_task = create_dataset()

    normalize_dataset_task = normalize_dataset(
        input_iris_dataset=create_dataset_task.outputs["iris_dataset"],
        scaler=scaler,
    )

    with dsl.ParallelFor(neighbors) as n_neighbors:
        train_model(
            normalized_iris_dataset=normalize_dataset_task.outputs[
                "normalized_iris_dataset"
            ],
            n_neighbors=n_neighbors,
            seed=seed,
        )


endpoint = "<KFP_UI_URL>"
kfp_client = client.Client(host=endpoint)
pipeline_run = kfp_client.create_run_from_pipeline_func(
    my_pipeline, arguments={"scaler": "min-max", "neighbors": [3, 6, 9]}
)
url = f"{endpoint}/#/runs/details/{pipeline_run.run_id}"
print(url)
```

Since the engineer defining the Kubeflow pipeline does not need to worry about the core logic of the nodes, they can focus on the orchestration-specific aspects.
For example, the Python dependencies for each component might be automatically taken from the project's packaging configuration (e.g., `pyproject.toml` or `requirements.txt`), rather than being hardcoded in the Kubeflow component definitions.
