# Docker

Docker furthermore obfuscates the intrinsics of the application for the user.
In essence, this means the user is not bothered [...]

## Making your project runnable

First, we need to make your application runnable.
That means we need to create an entrypoint that users can invoke.
In Python that entrypoint will be a `__main__.py` script at the source root:

```text
src
└── __main__.py
```

Ordeq provides two ways to run a project out of the box:

- through the command line interface (see `ordeq-cli-runner`)
- programmatically (built-in in `ordeq`)

A CLI is a good options if you need to dynamically decide which pipeline to run.
If your application always runs a single pipeline with the same configuration, it's easier to run that pipeline programmatically:
Of course, you can also create a custom CLI.
Click on the tabs below to see some example entrypoints.

=== "src/\_\_main\_\_.py (Ordeq CLI)"
    ```python
    from ordeq_cli_runner import main

    if __name__ == "__main__"
        main()
    ```

=== "src/\_\_main\_\_.py (Programmatic)"
    ```python
    import pipeline
    from ordeq import run

    if __name__ == "__main__"
        run(pipeline)
    ```

=== "src/\_\_main\_\_.py (Custom CLI)"
    ```python
    from argparse import ArgumentParser
    from ordeq import run

    if __name__ == "__main__"
        parser = ArgumentParser()
        parser.add_argument("--pipeline")
        args = parser.parse_args()
        run(args.pipeline)
    ```

This entrypoint makes the entire project runnable, not just for containers.

## Packaging your application
Next, we are going to package our application in a Docker container.
The first step is to determine the base image that your application will run on.
We recommend following the uv Docker guide to set up your base image and dependencies.

### Example

### Deciding the entrypoint
If you've opted for the CLI above, you likely want to keep the command with which the application is run dynamic.
This means the last line of the Dockerfile should contain the entrypoint to the application:

```Dockerfile

ENTRYPOINT ["uv", "run", "src/__main__.py", "run"]
```

If, on the other hand, your application run does not depend on the command with which it is invoked, you can specify the complete run command:

```Dockerfile
CMD ["uv", "run", "src/__main__.py"]
```

!!! "Configuration secrets"
    Docker provides multiple ways to configure application secrets, like API keys, passwords, and tokens.
    This configuration is not specific to Ordeq.
    We therefore refer to the Docker documentation.

## Running your application

Things to check:
- if your pipeline connects to external services, like S3 or a database, you need to alter the network configuration
- logging?

### Development containers

### Docker compose
Like any Docker container, you can also run the application using Docker compose.
This is particularly useful if the Ordeq application is part of a larger stack.
Say, you have a local database that you wish to test the Ordeq application on.

```yaml
services:
    db:
        ...
    app:
        ...

networks:
    - ...
```

You can run this stack with:

```bash
docker compose up
```
