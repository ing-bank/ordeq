# Using Marimo with Ordeq

[Marimo](https://docs.marimo.io/) is an open-source reactive Python notebook. An improved version of Jupyter notebooks, Marimo allows you to build data applications with interactive widgets and reactive cells.

This example demonstrates how to use Ordeq within a Marimo notebook to create an interactive data application.

Even though this examples is written for Marimo, you can run similar code in a Jupyter notebook as well.

```python {marimo display_code=true display_output=true is_reactive=false}
import marimo as mo

slider = mo.ui.slider(1, 10, value=5)
mo.md(f"Change the slider value: {slider}")
```


/// marimo-embed
    height: 400px
    mode: read

```python
@app.cell
def __():
    import marimo as mo

    name = mo.ui.text(placeholder="Enter your name", debounce=False)
    name
    return

@app.cell
def __():
    mo.md(f"Hello, **{name.value or '__'}**!")
    return
```
///



/// marimo-embed-file
    filepath: guides/examples/marimo/src/marimo_example.py
    height: 400px
    mode: read
    show_source: true
///
