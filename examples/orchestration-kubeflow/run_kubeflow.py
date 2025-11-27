from dataclasses import replace

from kfp import client, dsl
from ml_pipeline import catalog, preprocessing, train
from ordeq import run


@dsl.component(packages_to_install=["pandas==1.3.5"])
def create_dataset(iris_dataset: dsl.Output[dsl.Dataset]):
    run(
        preprocessing.create_dataset,
        io={
            catalog.csv_local: replace(
                catalog.csv_local, path=iris_dataset.path
            )
        },
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
            catalog.csv_local: replace(
                catalog.csv_local, path=input_iris_dataset.path
            ),
            catalog.csv_normalized: replace(
                catalog.csv_normalized, path=normalized_iris_dataset.path
            ),
            catalog.scaler: scaler,
        },
    )


@dsl.component(packages_to_install=["pandas==1.3.5", "scikit-learn==1.0.2"])
def train_model(
    normalized_iris_dataset: dsl.Input[dsl.Dataset],
    model: dsl.Output[dsl.Model],
    n_neighbors: int,
    seed: int | None,
):
    run(
        train.train_model,
        io={
            catalog.csv_normalized: replace(
                catalog.csv_normalized, path=normalized_iris_dataset.path
            ),
            catalog.knn_model: replace(catalog.knn_model, path=model.path),
            catalog.n_neighbors: n_neighbors,
            catalog.seed: seed,
        },
    )


@dsl.pipeline(name="iris-training-pipeline")
def my_pipeline(scaler: str, neighbors: list[int], seed: int | None):
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


if __name__ == "__main__":
    endpoint = "<KFP_UI_URL>"
    kfp_client = client.Client(host=endpoint)
    pipeline_run = kfp_client.create_run_from_pipeline_func(
        my_pipeline,
        arguments={"scaler": "min_max", "neighbors": [3, 6, 9], "seed": 0},
    )
    url = f"{endpoint}/#/runs/details/{pipeline_run.run_id}"
    print(url)
