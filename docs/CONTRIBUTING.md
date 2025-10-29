# Contributing

Thanks for considering to contribute to Ordeq!
All contributions are welcome, whether it's reporting issues, suggesting features, or submitting code changes.
This should get you started:

- Have a look at the [open issues][open-issues]
- Have a look at our guidelines below
- Set up your local environment as instructed below

## Guidelines

Feel free to challenge the below contributing guidelines.
We are young project and still figuring out how we can collaborate best.

### Development & testing

The `just` command runner tool is used for common tasks in the project.
After installing it, you can run `just` to see the available commands:

<!-- auto-generated justfile commands start -->

```text
Available recipes:
    localsetup                # Local installation
    ruff                      # Linting and formatting with ruff
    mdformat                  # Formatting with mdformat
    mdformat-fix              # Fix formatting with mdformat
    doccmd-ruff-format        # Formatting with ruff via doccmd
    doccmd-ruff-lint          # Linting with ruff via doccmd
    doccmd-fix                # Combine doccmd with ruff for linting and formatting
    lint                      # Linting with ruff
    lint-fix                  # Fix linting issues with ruff
    format                    # Formatting with ruff
    format-fix                # Fix formatting with ruff
    ty                        # Type checking with ty
    list                      # List all packages
    mypy                      # Type checking with mypy
    mypy-packages             # Mypy check all package directories
    mypy-examples             # Mypy check all example directories
    sa                        # Static analysis (lint + type checking)
    fix                       # Format code and apply lint fixes with ruff and mdformat
    test *PACKAGES            # or `just test ordeq ordeq-cli-runner` (Run tests in the 'ordeq' and 'ordeq-cli-runner' packages)
    test_package PACKAGE      # Test a single package
    test_all                  # Run tests for all packages with coverage
    generate-api-docs         # Generate API documentation pages
    generate-package-overview # Generate package overview documentation page
    docs-build                # Build the documentation
    docs-serve                # Build and serve the documentation locally
    docs-publish              # Publish the documentation to GitHub Pages
    precommit                 # Run pre-commit hooks
    precommit_install         # Install pre-commit hooks
    install                   # Install development dependencies
    upgrade                   # Upgrade (pre-commit only)
    build PACKAGE             # Build a package
    publish PACKAGE           # You need an API token from PyPI to run this command.
    lock                      # Lock dependencies
    bump *ARGS                # Bump version
    delete-snapshots          # Delete all .snapshot.md files anywhere in the repository
    capture-snapshots         # Recompute snapshots by running only those tests for all packages
```

<!-- auto-generated justfile commands end -->

Tip: install support for `just` in your IDE, e.g. [just for PyCharm](https://plugins.jetbrains.com/plugin/18658-just).

Install Ordeq locally in editable mode:

```shell
just localsetup
```

(In case of any issues, check out the troubleshooting section below)

Install the pre-commit hooks:

```shell
uv run pre-commit install
```

- When you start on a work item, create a new branch.
- The CI pipeline will be triggered when you create a pull request.
- Pull requests should merge your branch into `main`.
- You are encouraged to open and share draft PRs for work that is pending.
- The merge type must be squash commit.
- The pull request title and labels will be used to generate the release notes.
- There is a policy check on the PR which ensures that, before merge:
    - the build has succeeded (formatting, linters & tests pass)
    - open comments are resolved
    - at least one person besides the author has approved

### Releases

- We use [semantic versioning](http://semver.org/) for the release tags.
- Releases should be done for each package individually, e.g. `ordeq`,`ordeq-spark`
- Releases are managed via GitHub releases.
- To create releases:
    - Ensure you are on the `main` branch and have pulled the latest changes.
    - Run the release script `uv run scripts/generate_draft_releases.py`.
    - This will create draft releases for all packages that have changes since the last release.
    - Go to the "Releases" section of the GitHub repository.
    - Find the draft release for the package you want to publish.
    - Review the release notes and make any necessary edits.
    - Untick the "Set as the latest release" checkbox if you are not releasing the `ordeq` package.
    - Click "Publish release"
    - The CI will automatically build the package and upload it to Pypi.

### Publishing to PyPi for the first time

GitHub Actions cannot publish a new package to PyPi until GitHub is added as a Trusted Publisher for the project.
To enable automated publishing, you must first configure the Trusted Publisher settings:

- Add the new package as pending trusted publisher:
    - Go to https://pypi.org/manage/account/publishing/
    - Click "Add a new trusted publisher"
    - Enter the package name (e.g. `ordeq_spark`) as PyPi project name
    - Owner/Organization: `ing-bank`
    - Repository: `ordeq`
    - Workflow: `release.yml`
    - Environment: `pypi`
- After completing these steps, future tags pushed to the repository will trigger automated publishing via GitHub Actions.

### Troubleshooting

#### Locked dependencies

If you get an error saying: `error: Failed to parse 'uv.lock'` or `The lockfile at 'uv.lock' needs to be updated`,
this usually indicates that the dependencies were altered in the `pyproject.toml` or `uv.lock`.

- Please check if you have accidentally altered `pyproject.toml` or `uv.lock`
- Use `uv add` instead of (`uv`) `pip install`. More info [here](https://docs.astral.sh/uv/concepts/projects/dependencies/).

#### Non-pip dependencies

If you receive the following error installing `pymssql` on Mac,
you need to install FreeTDS to get the required C-headers: `brew install freetds`.

```text
  × Failed to build `pymssql==2.3.7`
  ├─▶ The build backend returned an error
  ╰─▶ Call to `setuptools.build_meta:__legacy__.build_wheel` failed (exit status: 1)
```

#### Docker-backed Tests

Some of the unit tests rely on Docker via the [`testcontainers`][tesco] PyPI package.
If you're using Docker Desktop on macOS, these tests will fail in the default configuration:

```text
ERROR tests/.../test_xxx.py::TestFile::test_function - docker.errors.DockerException: Error while fetching server API version: ('Connection aborted.', FileNotFoundError(2, 'No such file or directory'))
```

This can be remedied by changing the configuration of Docker Desktop for macOS:

1. Open Docker Desktop, go to Settings ⇒ Advanced
1. Enable "Docker CLI Tools System ⇒ (requires password)"
1. Enable "Allow default Docker socket (requires password)"
1. Click "Apply & Restart"

#### Spark & Java

The unit tests for `ordeq-spark` run Spark on your host system.
This means that Java must be installed on your laptop, and your default Java VM must not be newer than JDK 17, because newer versions remove some deprecated functions that Spark still relies on:

```text
E                   py4j.protocol.Py4JJavaError: An error occurred while calling None.org.apache.spark.api.java.JavaSparkContext.
E                   : java.lang.ExceptionInInitializerError
E                   	at org.apache.spark.unsafe.array.ByteArrayMethods.<clinit>(ByteArrayMethods.java:56)
                        ...
E                   Caused by: java.lang.NoSuchMethodException: java.nio.DirectByteBuffer.<init>(long,int)
                        ...
```

If you use [SdkMan!][sdkm] to manage your Java installations:

```shell
sdk list java | fgrep 17 | fgrep tem
sdk install java 17.0.12-tem   # replace 12 by whatever is current
sdk default java 17.0.12-tem
```

If you use another tool to manage your JDKs, run the equivalent tasks to make sure your `JAVA_HOME` is set correctly.

[open-issues]: https://github.com/ing-bank/ordeq/issues/
[sdkm]: https://sdkman.io/
[tesco]: https://pypi.org/project/testcontainers/
