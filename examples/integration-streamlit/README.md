# Streamlit integration for Ordeq

To run the Streamlit application:

1. Install the dependencies:

```bash
uv sync
```

2. Run the Streamlit app:

```bash
uv run streamlit run src/example/app.py
```

3. Open your web browser and navigate to `http://localhost:8501` to view the application.

Three widgets appear:

- A checkbox
- A slider
- A button

Once you click the button, a pipeline will be run.
The pipeline consists of one node that prints the values of the checkbox and slider to the console.

For instance:

```text
Checkbox is False
Slider value is 41
```
