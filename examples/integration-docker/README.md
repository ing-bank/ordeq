# Ordeq Docker integration

This example demonstrates how to integrate Ordeq with Docker to run pipelines in isolated container environments.

To run this example without building the Docker image:

```shell
uv run python -m integration_docker run integration_docker.pipeline:hello_world
```

To build the Docker image used in this example, run:

```shell
docker build -t app .
docker run app integration_docker.pipeline:hello_world
```

This will print 'Hello, World!' from within the Docker container.
