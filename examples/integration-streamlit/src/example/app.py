import streamlit as st
from ordeq import run

import example.pipeline


def on_click() -> None:
    run(example.pipeline)


st.checkbox("Checkbox", key="checkbox")
st.slider("Slider", 0, 100, key="slider")
st.button("Run pipeline", on_click=on_click)
