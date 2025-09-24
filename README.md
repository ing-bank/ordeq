# Welcome to Ordeq!

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

## Seamless integration

<!-- Data processing library logos -->
<div style="display: flex; gap: 40px; align-items: center; flex-wrap: wrap;">
  <img src="https://raw.githubusercontent.com/pandas-dev/pandas/main/web/pandas/static/img/pandas_mark.svg" alt="Pandas" height="40"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/f/f3/Apache_Spark_logo.svg" alt="Spark" height="40"/>
  <img src="https://numpy.org/images/logo.svg" alt="NumPy" height="40"/>
  <img src="https://www.pola.rs/assets/img/logo.svg" alt="Polars" height="40"/>
  <img src="https://ibis-project.org/_static/ibis-logo.svg" alt="Ibis" height="40"/>
  <img src="https://matplotlib.org/_static/images/logo2.svg" alt="Matplotlib" height="40"/>
  <img src="https://raw.githubusercontent.com/facebookresearch/faiss/main/resources/faiss_logo.png" alt="Faiss" height="40"/>
  <img src="https://joblib.readthedocs.io/en/latest/_static/joblib-logo-light.svg" alt="Joblib" height="40"/>
  <img src="https://huggingface.co/front/assets/huggingface_logo.svg" alt="HuggingFace" height="40"/>
  <img src="https://pymupdf.readthedocs.io/en/latest/_static/logo.png" alt="PyMuPDF" height="40"/>
  <img src="https://www.sbert.net/_static/logo.png" alt="SentenceTransformers" height="40"/>
  <img src="https://boto3.amazonaws.com/v1/documentation/api/latest/_static/boto3.png" alt="Boto3" height="40"/>
  <img src="https://requests.readthedocs.io/en/latest/_static/requests-logo.png" alt="Requests" height="40"/>
</div>

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
