from dataclasses import dataclass
from typing import TypeVar

import streamlit as st
from ordeq import Input

T = TypeVar("T")


@dataclass(frozen=True)
class StreamlitElement(Input[T]):
    key: str | int

    def load(self) -> T:
        """Loads the value from the Streamlit session state.

        Returns:
            The value associated with the specified key in the session state.

        Raises:
            StreamlitAPIException:
                If the specified key does not exist in the session state.
        """  # noqa: DOC502 (exception not explicitly raised)
        return st.session_state[self.key]
