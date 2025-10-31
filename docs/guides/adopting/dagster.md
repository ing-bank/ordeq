# Coming from Dagster

This guide is for users familiar with Dagster who want to get started with Ordeq.

- Dagster is also a data orchestrator, while Ordeq focuses on streamlining data engineering tasks with a simpler and more flexible approach.
    This means that Dagster has additional built-in features, such as schedules, run tracking and sensors, that are not present in Ordeq.
    Instead, Ordeq integrates seamlessly with existing scheduling and monitoring tools, such as Dagster, Airflow and KubeFlow, allowing you to leverage your current infrastructure.
    Writing your code in Ordeq is often more straightforward and requires less boilerplate compared to concept-heavy Dagster.
    This reduces the learning curve and accelerates development time.
    Because of the above distinction, Dagster also has more dependencies (49 at the time of writing) compared to the lightweight Ordeq (none).

- Ordeq tries to leverage native Python features as much as possible, while Dagster often requires using its own abstractions.
    This means that in Ordeq you can use standard Python libraries and tools without needing to adapt them to Dagster's framework.
    This results in more readable and maintainable code, as you can rely on familiar Python constructs.

## Assets vs IOs

- Dagster: function-based assets, four decorators https://docs.dagster.io/guides/build/assets/defining-assets
- Ordeq: single `@node` decorator with IOs. IOs are classes (with attributes for state).

## Example project

For this guide we use the "project_ml" example project from the Dagster repository, and show how the same functionality can be implemented in Ordeq.
The original Dagster example can be found [here](https://github.com/dagster-io/dagster/tree/master/examples/docs_projects/project_ml).

```text title="Dagster project structure"
.
├── pyproject.toml
├── src
│   └── project_ml
│       ├── __init__.py
│       ├── definitions.py
│       └── defs
│           ├── __init__.py
│           ├── asset_checks.py
│           ├── assets
│           │   ├── __init__.py
│           │   ├── data_assets.py
│           │   ├── model_assets.py
│           │   └── prediction_assets.py
│           ├── constants.py
│           ├── jobs.py
│           ├── resources.py
│           ├── schedules.py
│           ├── sensors.py
│           ├── types.py
│           └── utils.py
└── tests
    ├── __init__.py
    ├── conftest.py
    ├── test_data_assets.py
    ├── test_full_pipeline.py
    └── test_model.py
```


```text title="Ordeq project structure"
.
├── data
│   └── 01_raw
├── pyproject.toml
├── src
│   └── project_ml
│       ├── __init__.py
│       ├── __main__.py
│       ├── catalog.py
│       ├── config
│       │   ├── __init__.py
│       │   ├── batch_prediction_config.py
│       │   ├── deployment_config.py
│       │   ├── model_config.py
│       │   ├── model_evaluation_config.py
│       │   └── real_time_prediction_config.py
│       ├── data
│       │   ├── __init__.py
│       │   ├── data_preprocessing.py
│       │   └── raw_data_loading.py
│       ├── deploy
│       │   ├── __init__.py
│       │   ├── deploy_model.py
│       │   └── predict.py
│       └── model
│           ├── __init__.py
│           ├── cnn_architecture.py
│           ├── digit_classifier.py
│           ├── model_evaluation.py
│           └── train_model.py
└── tests
```

Deviations:
- excluded model selection part for simplicity
- data quality checks

## Context

Dagster uses "context" which requires a global variable to be passed around.
Ordeq avoids this pattern by allowing nodes to request IOs directly.
For example, metadata in Ordeq is just another IO that contains the metadata information, instead of a dedicated `context.add_output_metadata`
See [parametrizing nodes] for more details.

## Logging

In Dagster you would write:

```python
context.log.info(
    f"User requested deployment of custom model: {config.custom_model_name}"
)
```

In most cases in Ordeq this becomes native Python logging:

```python
import logging

logger = logging.getLogger(__name__)

# (...)

logger.info(
    f"User requested deployment of custom model: {config.custom_model_name}"
)
```

Only when you need advanced structured logging features you would use Ordeq's `Logger` IO.

## Configuration

Dagster requires user to use own objects `dg.Config`, whereas in Ordeq you can use
native Python types for configuration (constants, files, dataclasses, Pydantic or whatever your preference has).

## Attributes

```python
@dg.asset(
    description="Evaluate model performance on test set",
    group_name="model_pipeline",
    required_resource_keys={"model_storage"},
    deps=["digit_classifier"],
    ...
)
```

```python
@node(..., description="Evaluate model performance on test set")
```

The other attributes are not required, as `group_name` in inferred from the module name, and `required_resources_keys` and `deps` from the node inputs and outputs.

## Cloud integration

The Dagster example implements dedicated resources for S3 and local file system:
https://github.com/dagster-io/dagster/blob/master/examples/docs_projects/project_ml/src/project_ml/defs/resources.py

In Ordeq you can use the same code for both local and S3 storage by leveraging the existing IOs.
(see [Storage IOs] for more details).

## Asset checks

Dagster has built-in asset checks, while in Ordeq you can implement similar functionality using nodes that validate data and raise exceptions if checks fail.
https://github.com/dagster-io/dagster/blob/master/examples/docs_projects/project_ml/src/project_ml/defs/asset_checks.py

For this guide we keep it out of scope.
