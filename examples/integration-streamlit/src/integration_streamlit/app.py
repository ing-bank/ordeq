import streamlit as st
from ordeq import run

import integration_streamlit.pipeline


def on_click() -> None:
    """Callback function to run the pipeline when the button is clicked."""
    run(integration_streamlit.pipeline)


st.checkbox("Checkbox", key="checkbox")
st.slider("Slider", 0, 100, key="slider")
st.button("Run pipeline", on_click=on_click)
