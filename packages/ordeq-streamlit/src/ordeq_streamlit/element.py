import streamlit as st
from typing import TypeVar
from ordeq import Input
from dataclasses import dataclass

T = TypeVar("T")


@dataclass(frozen=True)
class StreamlitElement(Input[T]):
    key: str | int

    def load(self) -> T:
        """Loads the value from the Streamlit session state."""
        return st.session_state[self.key]
