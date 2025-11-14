# ruff: noqa
import marimo

__generated_with = "0.17.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Ordeq

    Ordeq is a framework for developing data pipelines. It simplifies IO and modularizes pipeline logic.
    """
    )


@app.cell
def _(mo):
    mo.md(
        r"""
    Ordeq allows you to focus only on the business logic required for your pipeline and not on the I/O operations.

    First, you define what is the Input data your pipeline needs as well as the what Output data that your pipeline produces. These are your **IO objects**.

    Typically you'd put them in a file called `catalog.py`
    """
    )


@app.cell
def _():
    # catalog.py
    from pathlib import Path

    from ordeq_polars import PolarsEagerCSV

    data_dir = Path(__file__).parent / "data"
    data_dir.mkdir(exist_ok=True)

    # Input data
    user_data = PolarsEagerCSV(path=data_dir / "users.csv")

    # Output data
    clean_users_data = PolarsEagerCSV(path=data_dir / "clean_users.csv")
    user_metrics = PolarsEagerCSV(path=data_dir / "user_metrics.csv")
    return clean_users_data, user_data, user_metrics


@app.cell
def _(mo):
    mo.md(
        r"""Let's first create a Polars DataFrame containing our user data, then use the `PolarsEagerCSV` IO to write it to a CSV file."""
    )


@app.cell
def _():
    import polars as pl

    user_data_df = pl.DataFrame([
        {
            "Name": "John Doe",
            "Email": "john@example.com",
            "Phone": "555-123-4567",
        },
        {
            "Name": "Jane Smith",
            "Email": "jane@example.com",
            "Phone": "555-987-6543",
        },
        {
            "Name": "Peter Jones",
            "Email": "peter@sample.com",
            "Phone": "555-555-1212",
        },
        {
            "Name": "Rachel Adams",
            "Email": "rachel.adams@test.com",
            "Phone": "555-444-3333",
        },
        {
            "Name": "Emily Davis",
            "Email": "emily.davis@sample.com",
            "Phone": "555-333-2222",
        },
        {
            "Name": "Michael Brown",
            "Email": "michael.brown@example2.com",
            "Phone": "555-222-1111",
        },
        {
            "Name": "Jane L. Smith",
            "Email": "jane@example.com",
            "Phone": "555-987-6543",
        },
    ])
    user_data_df
    return pl, user_data_df


@app.cell
def _(user_data, user_data_df):
    # Write the data to a file using the IO object's .save() method:
    user_data.save(user_data_df)


@app.cell
def _(user_data):
    # You can also load the data from using the IO object's .load() method:

    user_data.load()


@app.cell
def _(mo):
    mo.md(
        r"""
    **Nodes** are Python functions decorated with `@node`, which implement the business logic of your pipeline.

    Ordeq automatically loads and passes the `IO` objects that you mark as `inputs` of the node to the function and saves the data returned by the function to the `IO` objects marked as `outputs`. This way you don't need to worry about the inputs and outputs of your transformations and only focus on the business logic of your application.
    """
    )


@app.cell
def _(clean_users_data, pl, user_data, user_metrics):
    # nodes.py
    from ordeq import node
    from polars import DataFrame

    @node(inputs=[user_data], outputs=[clean_users_data])
    def clean_users(user_data_df: DataFrame) -> DataFrame:
        return user_data_df.select(
            pl.col("Name").alias("name"),
            pl.col("Email").alias("email"),
            pl.col("Phone").alias("phone"),
            pl.col("Email").str.split("@").list.get(-1).alias("email_domain"),
        )

    @node(inputs=[clean_users_data], outputs=[user_metrics])
    def extract_user_metrics(clean_users_df: DataFrame) -> DataFrame:
        return clean_users_df.select(
            pl.len().alias("user_cnt"),
            pl.col("email").n_unique().alias("unique_users"),
            pl.col("email_domain").n_unique().alias("unique_email_domains"),
            pl.col("phone").n_unique().alias("unique_phone_numbers"),
        )

    return clean_users, extract_user_metrics


@app.cell
def _(mo):
    mo.md(
        r"""You can visualize the pipeline you've built by using the `ordeq-viz` package"""
    )


@app.cell
def _(clean_users, extract_user_metrics, mo):
    from ordeq_viz import viz

    diagram = viz(clean_users, extract_user_metrics, fmt="mermaid")
    mo.mermaid(diagram)


@app.cell
def _(mo):
    mo.md(
        r"""Then run the pipeline by using `ordeq.run`, which takes the same arguments as `viz`"""
    )


@app.cell
def _(clean_users, extract_user_metrics):
    from ordeq import run

    run(clean_users, extract_user_metrics)


@app.cell
def _(mo):
    mo.md(r"""Inspect the saved outputs""")


@app.cell
def _(clean_users_data):
    clean_users_data.load()


@app.cell
def _(user_metrics):
    user_metrics.load()


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
