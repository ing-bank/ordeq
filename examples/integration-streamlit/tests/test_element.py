import pytest
import streamlit as st
from ordeq import IOException
from example.io import StreamlitElement


def test_it_loads():
    st.session_state["slider"] = "test_it_loads"
    element = StreamlitElement(key="slider")
    assert element.load() == "test_it_loads"


def test_key_doesnt_exist():
    with pytest.raises(
        IOException,
        match=r'st.session_state has no key "idontexist". '
              r"Did you forget to initialize it?",
    ):
        _ = StreamlitElement(key="idontexist").load()


def test_its_hashable():
    a = StreamlitElement(key="a")
    b = StreamlitElement(key="b")
    assert hash(a) != hash(b)
    assert a != b
