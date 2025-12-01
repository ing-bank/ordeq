# Kubeflow orchestration example

This example demonstrates how to integrate Ordeq with Kubeflow Pipelines for orchestrating machine learning workflows in Kubernetes clusters.

## Running the pipeline

### Local execution

To run the pipeline locally:

```bash
uv run run_local.py
```

This will execute the entire pipeline on your local machine using Ordeq's standard runner.

### Kubeflow execution

To run on Kubeflow Pipelines:

1. Update the `endpoint` variable in `run_kubeflow.py` with your Kubeflow Pipelines UI URL
2. Ensure you have access to a Kubeflow cluster
3. Run:

```bash
uv run run_kubeflow.py
```
