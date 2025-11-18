# Welcome to Ordeq!

[![Release](https://github.com/ing-bank/ordeq/actions/workflows/release.yml/badge.svg?event=push)](https://github.com/ing-bank/ordeq/actions/workflows/release.yml)
[![Docs](https://github.com/ing-bank/ordeq/actions/workflows/docs.yml/badge.svg)](https://github.com/ing-bank/ordeq/actions/workflows/docs.yml)
[![PyPI](https://img.shields.io/pypi/v/ordeq?label=ordeq)](https://pypi.org/project/ordeq/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/ordeq?label=downloads)](https://pypistats.org/packages/ordeq)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Static Badge](https://img.shields.io/badge/powered_by-Ordeq-darkgreen?style=flat&link=https%3A%2F%2Fing-bank.github.io%2Fordeq%2F)](https://github.com/ing-bank/ordeq)

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

## Integrations

Ordeq integrates seamlessly with existing tooling.
It provides integrations with many popular libraries out of the box.
You can install them as needed.
For example, for reading and writing data with Pandas, install the `ordeq-pandas` package:

```shell
uv pip install ordeq-pandas
```

Some of the available integrations:

**Data processing**

<table>
    <tr>
        <td width="90" height="60" align="center">
            <a href="https://ing-bank.github.io/ordeq/api/ordeq_pandas/"><img src="https://raw.githubusercontent.com/pandas-dev/pandas/main/web/pandas/static/img/pandas_mark.svg" alt="Pandas" height="40"/><br />Pandas</a>
        </td>
        <td width="90" height="60" align="center">
            <a href="https://ing-bank.github.io/ordeq/api/ordeq_spark/"><img src="https://icon.icepanel.io/Technology/svg/Apache-Spark.svg" alt="Spark" height="40"/><br />Spark</a>
        </td>
        <td width="90" height="60" align="center">
            <a href="https://ing-bank.github.io/ordeq/api/ordeq_numpy/"><img src="https://numpy.org/images/logo.svg" alt="NumPy" height="40"/><br />Numpy</a>
        </td>
        <td width="90" height="60" align="center">
            <a href="https://ing-bank.github.io/ordeq/api/ordeq_polars/"><img src="https://avatars.githubusercontent.com/u/83768144?s=200&v=4" alt="Polars" height="60"/><br />Polars</a>
        </td>
        <td width="90" height="60" align="center">
            <a href="https://ing-bank.github.io/ordeq/api/ordeq_ibis/"><img src="https://ibis-project.org/logo.svg" alt="Ibis" height="50"/><br />Ibis</a>
        </td>
        <td width="90" height="60" align="center">
            <a href="https://ing-bank.github.io/ordeq/api/ordeq_joblib/"><img src="https://joblib.readthedocs.io/en/stable/_static/joblib_logo.svg" alt="Joblib" height="40"/><br />Joblib</a>
        </td>
        <td width="90" height="60" align="center">
            <a href="https://ing-bank.github.io/ordeq/api/ordeq_huggingface/"><img src="https://huggingface.co/front/assets/huggingface_logo.svg" alt="HuggingFace" height="40"/><br />HuggingFace</a>
        </td>
        <td width="90" height="60" align="center">
            <a href="https://ing-bank.github.io/ordeq/api/ordeq_pillow/"><img src="https://pillow.readthedocs.io/en/stable/_static/pillow-logo.png" alt="Pillow" height="40"/><br />Pillow</a>
        </td>
    </tr>
    <tr>
        <td width="90" height="60" align="center">
            <a href="https://ing-bank.github.io/ordeq/api/ordeq_sentence_transformers/"><img src="https://www.sbert.net/_static/logo.png" alt="SentenceTransformers" height="40"/><br />st</a>
        </td>
        <td width="90" height="60" align="center">
            <a href="https://ing-bank.github.io/ordeq/api/ordeq_requests/"><img src="https://upload.wikimedia.org/wikipedia/commons/a/aa/Requests_Python_Logo.png" alt="Requests" height="50"/><br />Requests</a>
        </td>
        <td width="90" height="60" align="center">
            <a href="https://ing-bank.github.io/ordeq/api/ordeq_pydantic/"><img src="https://avatars.githubusercontent.com/u/110818415?v=4" alt="Pydantic" height="40"/><br />Pydantic</a>
        </td>
        <td width="90" height="60" align="center">
            <a href="https://ing-bank.github.io/ordeq/api/ordeq_duckdb/"><img src="https://assets.streamlinehq.com/image/private/w_300,h_300,ar_1/f_auto/v1/icons/logos/duckdb-umoj5fxu8w5pzg7d0js9.png/duckdb-kz05ottxukbgvmp8c3bpi.png?_a=DATAg1AAZAA0" alt="DuckDB" height="40"/><br/>DuckDB</a>
        </td>
        <td width="90" height="60" align="center">
            <a href="https://ing-bank.github.io/ordeq/api/ordeq_networkx/"><img src="https://avatars.githubusercontent.com/u/388785?s=200&v=4" alt="Networkx" height="40"/><br/>NetworkX</a>
        </td>
        <td width="90" height="60" align="center">
            <a href="https://ing-bank.github.io/ordeq/api/ordeq_toml/"><img src="https://upload.wikimedia.org/wikipedia/commons/c/c1/TOML_Logo.svg" alt="TOML" height="40"/><br/>TOML</a>
        </td>
        <td width="90" height="60" align="center">
            <a href="https://ing-bank.github.io/ordeq/api/ordeq_pymupdf/"><img src="https://pymupdf.readthedocs.io/en/latest/_static/sidebar-logo-light.svg" alt="PyMuPDF" height="40"/><br />PyMuPDF</a>
        </td>
    </tr>
</table>

**Plotting**

<table>
    <tr>
        <td width="90" height="60" align="center">
            <a href="https://ing-bank.github.io/ordeq/api/ordeq_matplotlib/"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Created_with_Matplotlib-logo.svg/2048px-Created_with_Matplotlib-logo.svg.png" alt="Matplotlib" height="40"/><br />Matplotlib</a>
        </td>
        <td width="90" height="60" align="center">
            <a href="https://ing-bank.github.io/ordeq/api/ordeq_altair/"><img src="https://avatars.githubusercontent.com/u/22396732?s=200&v=4" alt="Altair" height="40"/><br/>Altair</a>
        </td>
        <td width="90" height="60" align="center">
            <a href="https://ing-bank.github.io/ordeq/api/ordeq_plotly_express/"><img src="https://upload.wikimedia.org/wikipedia/commons/8/8a/Plotly-logo.png" alt="Plotly Express" height="40"/><br/>Plotly Express</a>
        </td>
    </tr>
</table>

**Cloud storage**

<table>
  <tr>
    <td width="180" height="60" align="center">
      <a href="https://ing-bank.github.io/ordeq/guides/cloud_storage/"><img src="https://1.bp.blogspot.com/-ldXyw__3o8k/XkTq7ynek6I/AAAAAAAATvQ/BMLEAwGefP8tA9YkpVRlfhj8q01qcDWsQCLcBGAsYHQ/s1600/gcp-bucket.png" alt="Google Cloud Storage" height="40"/><br />Google Cloud Storage</a>
    </td>
    <td width="180" height="60" align="center">
      <a href="https://ing-bank.github.io/ordeq/guides/cloud_storage/"><img src="https://logos-world.net/wp-content/uploads/2021/02/Microsoft-Azure-Emblem.png" alt="Azure" height="40"/><br />Azure Storage Blob</a>
    </td>
    <td width="180" height="60" align="center">
      <a href="https://ing-bank.github.io/ordeq/guides/cloud_storage/"><img src="https://freepngdesign.com/content/uploads/images/p-1692-1-aws-s3-logo-png-transparent-logo-585854250269.png" alt="AWS S3" height="40"/><br />AWS S3</a>
    </td>
    <td width="180" height="60" align="center">
      <a href="https://ing-bank.github.io/ordeq/api/ordeq_boto3/"><img src="https://boto3typed.gallerycdn.vsassets.io/extensions/boto3typed/boto3-ide/0.5.4/1680224848596/Microsoft.VisualStudio.Services.Icons.Default" alt="Boto3" height="40"/><br />Boto3</a>
    </td>
  </tr>
</table>

Have a look at the [package overview][packages] and [API reference][api-ref] for a list of available packages.

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
- Explore the [example projects][example-projects] to see how Ordeq is used

## Acknowledgements

Ordeq builds upon design choices and ideas from [Kedro] and other frameworks.
It has been developed at ING, with contributions from various individuals.
Please refer to the [acknowledgements] section in the documentation for more details.

[acknowledgements]: https://ing-bank.github.io/ordeq/contributing/acknowledgements/
[api-ref]: https://ing-bank.github.io/ordeq/api/ordeq/
[core-concepts]: https://ing-bank.github.io/ordeq/getting-started/concepts/io/
[example-projects]: https://github.com/ing-bank/ordeq/tree/main/examples
[intro]: https://ing-bank.github.io/ordeq/getting-started/introduction/
[kedro]: https://github.com/kedro-org/kedro
[license]: https://github.com/ing-bank/ordeq/blob/main/LICENSE
[notice]: https://github.com/ing-bank/ordeq/blob/main/NOTICE
[packages]: https://ing-bank.github.io/ordeq/packages/
