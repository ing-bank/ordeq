# Welcome to Ordeq!

[![Build](https://github.com/ing-bank/ordeq/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/ing-bank/ordeq/actions/workflows/build.yml)
[![Docs](https://github.com/ing-bank/ordeq/actions/workflows/publish-docs.yml/badge.svg)](https://github.com/ing-bank/ordeq/actions/workflows/publish-docs.yml)
![PyPI](https://img.shields.io/pypi/v/ordeq?label=pypi%20package)

Ordeq is a framework for developing data pipelines.
It simplifies IO and modularizes pipeline logic.
Ordeq elevates your proof-of-concept to a production-grade pipelines.
See the [introduction][intro] for an easy-to-follow example of how Ordeq can help.

## Installation

Ordeq is available under MIT license.
Please refer to the [license][license] and [notice][notice] for more details.

To install Ordeq, run:

```shell
uv pip install ordeq
```

## Integrations
Ordeq integrates seamlessly with existing tooling.
It provides integrations with many popular libraries out of the box.
You can install them as needed.
For example, for reading and writing data with Pandas, install the `ordeq-pandas` package:

```shell
uv pip install ordeq-pandas
```

Some of the available integrations:

<!-- Data processing library logos -->
<table>
  <tr>
    <td width="80" height="60" align="center"><img src="https://raw.githubusercontent.com/pandas-dev/pandas/main/web/pandas/static/img/pandas_mark.svg" alt="Pandas" height="40"/>Pandas</td>
    <td width="80" height="60" align="center"><img src="https://icon.icepanel.io/Technology/svg/Apache-Spark.svg" alt="Spark" height="40"/>Spark</td>
    <td width="80" height="60" align="center"><img src="https://numpy.org/images/logo.svg" alt="NumPy" height="40"/>Numpy</td>
    <td width="80" height="60" align="center"><img src="https://avatars.githubusercontent.com/u/83768144?s=200&v=4" alt="Polars" height="60"/>Polars</td>
    <td width="80" height="60" align="center"><img src="https://ibis-project.org/logo.svg" alt="Ibis" height="50"/>Ibis</td>
   <td width="80" height="60" align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Created_with_Matplotlib-logo.svg/2048px-Created_with_Matplotlib-logo.svg.png" alt="Matplotlib" height="40"/>Matplotlib</td>
    <td width="80" height="60" align="center"><img src="https://joblib.readthedocs.io/en/stable/_static/joblib_logo.svg" alt="Joblib" height="40"/>Joblib</td>
<td width="80" height="60" align="center"><img src="https://huggingface.co/front/assets/huggingface_logo.svg" alt="HuggingFace" height="40"/>HuggingFace</td>
  </tr>
  <tr>
    <td width="80" height="60" align="center"><img src="https://pymupdf.readthedocs.io/en/latest/_static/sidebar-logo-light.svg" alt="PyMuPDF" height="40"/>PyMuPDF</td>
    <td width="80" height="60" align="center"><img src="https://www.sbert.net/_static/logo.png" alt="SentenceTransformers" height="40"/>st</td>
    <td width="80" height="60" align="center"><img src="https://boto3.amazonaws.com/v1/documentation/api/latest/_static/logos/aws_dark_theme_logo.svg" alt="Boto3" height="40"/>AWS</td>
    <td width="80" height="60" align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/a/aa/Requests_Python_Logo.png" alt="Requests" height="50"/>Requests</td>
    <td width="80" height="60" align="center"><img src="https://cloud.google.com/_static/cloud/images/social-icon-google-cloud-1200-630.png" alt="Google Cloud" height="40"/>GCP</td>
    <td width="80" height="60" align="center"><img src="https://avatars.githubusercontent.com/u/110818415?v=4" alt="Pydantic" height="40"/>Pydantic</td>
    <td width="80" height="60" align="center"><img src="https://raw.githubusercontent.com/apache/parquet-format/25f05e73d8cd7f5c83532ce51cb4f4de8ba5f2a2/logo/parquet-logos_1.svg" alt="Parquet" height="50"/>Parquet</td>
 <td width="80" height="60" align="center"><img src="https://logos-world.net/wp-content/uploads/2021/02/Microsoft-Azure-Emblem.png" alt="Azure" height="40"/>Azure</td>
  </tr>
</table>

Have a look at the [API reference][api-ref] for a list of available packages.

## Documentation
Documentation is available at https://ing-bank.github.io/ordeq/.

## Why consider Ordeq?

- Ordeq is **the GenAI companion**: it gives your project structure and consistency, such that GenAI can thrive
- It offers **seamless integrations** with existing data & ML tooling, such as Spark, Pandas, Pydantic and PyMuPDF, and
  adding new integrations is trivial
- It's **actively developed** and **trusted** by data scientists, engineers, analysts and machine learning engineers at ING

## Learning Ordeq

To learn more about Ordeq, check out the following resources:

- See how Ordeq can help your project in the [introduction][intro]
- Check out the [core concepts][core-concepts] to learn how to use Ordeq
- Explore the [example project][example-project] to see how Ordeq is used

[core-concepts]: https://ing-bank.github.io/ordeq/getting-started/concepts/io/

[api-ref]: https://ing-bank.github.io/ordeq/api/ordeq/framework/io/

[intro]: https://ing-bank.github.io/ordeq/getting-started/introduction/

[example-project]: docs/guides/examples/example-project/README.md

[license]: ./LICENSE

[notice]: ./NOTICE
