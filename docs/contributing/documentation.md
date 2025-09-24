# Documentation

Ordeq uses [MkDocs](https://www.mkdocs.org/) for documentation, and [mkdocstrings](https://mkdocstrings.github.io/) for auto-generating the API documentation.
The documentation is configured in `mkdocs.yml` at the root of the repository.

To view the documentation locally, first install all dependencies:

```
just install
```

Next, generate the API documentation:

```shell
uv run python scripts/generate_api_docs.py
```

To spin up the documentation server, run:

```shell
uv run mkdocs serve
```

Optionally, use the `--strict` flag that causes the build fail on warnings, for instance due to missing links.

Now navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and enjoy the documentation!
