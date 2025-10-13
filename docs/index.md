# Welcome to Ordeq!

Ordeq is a framework for developing data pipelines.
It simplifies IO and modularizes pipeline logic.
Ordeq elevates your proof-of-concept to a production-grade pipelines.
See the [introduction][intro] for an easy-to-follow example of how Ordeq can help.

## Installation

Ordeq is available under MIT license.
Please refer to the [license] and [notice] for more details.

To install Ordeq, run:

```shell
uv pip install ordeq
```

Ordeq supports various IO packages for reading and writing data.
You can install them as needed.
For example, for reading and writing CSV files with Pandas, install the `ordeq-pandas` package:

```shell
uv pip install ordeq-pandas
```

Have a look at the [API reference][api-ref] for a list of available packages and extensions.

## Why consider Ordeq?

- Ordeq is **the GenAI companion**: it gives your project structure and consistency, such that GenAI can thrive
- It offers **seamless integrations** with existing data & ML tooling, such as Spark, Pandas, Pydantic and PyMuPDF, and
    adding new integrations is trivial
- It's **actively developed** and **trusted** by data scientists, engineers, analysts and machine learning engineers at
    ING

## Learning Ordeq

To learn more about Ordeq, check out the following resources:

- See how Ordeq can help your project in the [introduction][intro]
- Check out the [core concepts][core-concepts] to learn how to use Ordeq

[api-ref]: api/ordeq/types.md
[core-concepts]: getting-started/concepts/io.md
[intro]: getting-started/introduction.md
[license]: https://github.com/ing-bank/ordeq/blob/main/LICENSE
[notice]: https://github.com/ing-bank/ordeq/blob/main/NOTICE
