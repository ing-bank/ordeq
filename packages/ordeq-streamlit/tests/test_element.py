import streamlit as st

from ordeq_streamlit import StreamlitElement
import pytest
from ordeq import IOException


def test_it_loads():
    st.session_state["slider"] = "test_it_loads"
    element = StreamlitElement(key="slider")
    assert element.load() == "test_it_loads"


def test_key_doesnt_exist():
    st.button("test_key_doesnt_exist", key="a")
    with pytest.raises(
        IOException,
        match=r'st.session_state has no key "b". Did you forget to initialize it?'
    ):
        _ = StreamlitElement(key="b").load()


def test_its_hashable():
    a = StreamlitElement(key="a")
    b = StreamlitElement(key="b")
    assert hash(a) != hash(b)
    assert a != b
