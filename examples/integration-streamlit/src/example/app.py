import pipeline
import streamlit as st
from ordeq import run

st.checkbox("Checkbox", key="checkbox")
st.slider("Slider", 0, 100, key="slider")
st.button("Run pipeline", on_click=lambda: run(pipeline))
