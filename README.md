# Welcome to Ordeq!

[![Publish documentation](https://github.com/ing-bank/ordeq/actions/workflows/publish-docs.yml/badge.svg)](https://github.com/ing-bank/ordeq/actions/workflows/publish-docs.yml)

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

<!-- Data processing library logos -->
<table>
  <tr>
    <td width="80" height="60" align="center"><img src="https://raw.githubusercontent.com/pandas-dev/pandas/main/web/pandas/static/img/pandas_mark.svg" alt="Pandas" height="40"/></td>
    <td width="80" height="60" align="center"><img src="https://icon.icepanel.io/Technology/svg/Apache-Spark.svg" alt="Spark" height="40"/></td>
    <td width="80" height="60" align="center"><img src="https://numpy.org/images/logo.svg" alt="NumPy" height="40"/></td>
    <td width="80" height="60" align="center"><img src="https://avatars.githubusercontent.com/u/83768144?s=200&v=4" alt="Polars" height="40"/></td>
    <td width="80" height="60" align="center"><img src="https://ibis-project.org/logo.svg" alt="Ibis" height="40"/></td>
  </tr>
  <tr>
    <td width="80" height="60" align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Created_with_Matplotlib-logo.svg/2048px-Created_with_Matplotlib-logo.svg.png" alt="Matplotlib" height="40"/></td>
    <td width="80" height="60" align="center"><img src="https://joblib.readthedocs.io/en/stable/_static/joblib_logo.svg" alt="Joblib" height="40"/></td>
    <td width="80" height="60" align="center"><img src="https://huggingface.co/front/assets/huggingface_logo.svg" alt="HuggingFace" height="40"/></td>
    <td width="80" height="60" align="center"><img src="https://pymupdf.readthedocs.io/en/latest/_static/sidebar-logo-light.svg" alt="PyMuPDF" height="40"/></td>
    <td width="80" height="60" align="center"><img src="https://www.sbert.net/_static/logo.png" alt="SentenceTransformers" height="40"/></td>
  </tr>
  <tr>
    <td width="80" height="60" align="center"><img src="https://boto3.amazonaws.com/v1/documentation/api/latest/_static/logos/aws_dark_theme_logo.svg" alt="Boto3" height="40"/></td>
    <td width="80" height="60" align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/a/aa/Requests_Python_Logo.png" alt="Requests" height="40"/></td>
    <td width="80" height="80" align="center"><img src="https://cloud.google.com/_static/cloud/images/social-icon-google-cloud-1200-630.png" alt="Google Cloud" height="40"/></td>
    <td width="80" height="60" align="center"><img src="https://avatars.githubusercontent.com/u/110818415?v=4" alt="Pydantic" height="40"/></td>
    <td width="80" height="60" align="center"><img src="https://api.nuget.org/v3-flatcontainer/parquet.net/4.22.0/icon" alt="Parquet" height="40"/></td>
 <td height="60"><img src="https://logos-world.net/wp-content/uploads/2021/02/Microsoft-Azure-Emblem.png" alt="Azure"/></td>
  </tr>
</table>

Ordeq integrates seamlessly with existing tooling.
It provides integrations with many popular libraries out of the box.
You can install them as needed.
For example, for reading and writing data with Pandas, install the `ordeq-pandas` package:

```shell
uv pip install ordeq-pandas
```

Have a look at the [API reference][api-ref] for the documentation of each package.

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
- Explore the [example project][example-project] to see how Ordeq is used

[core-concepts]: docs/getting-started/concepts/io.md

[api-ref]: docs/api/ordeq/types.md

[intro]: docs/getting-started/introduction.md

[example-project]: docs/guides/examples/example-project/README.md

[license]: ./LICENSE

[notice]: ./NOTICE
