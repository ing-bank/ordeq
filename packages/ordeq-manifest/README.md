# ordeq-manifest

This package can be used to produce a manifest of an Ordeq project.
The manifest is a reproducible representation of the project.
It contains project metadata, such as which nodes and IOs are used.

The primary purpose of the manifest is to support Ordeq extensions, like `ordeq-viz` and `ordeq-airflow`.
For instance, `ordeq-viz` can use the manifest to create a visualization of the project.
Similarly, `ordeq-airflow` can use the manifest to create Airflow DAGs.

## Installation

To install `ordeq-manifest` from the PyPi registry, run:

```bash
uv pip install ordeq-manifest
```

## Development status

This package is currently in beta stage.
Please report any issues or requests on the [GitHub repository][github-repo].

## License

This package is distributed under MIT license.
Please refer to the [license] and [notice] for more details.

[license]: ./LICENSE
[notice]: ./NOTICE
[github-repo]: https://github.com/ing-bank/ordeq/issues
