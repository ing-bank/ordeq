import catalog
from ordeq import node


@node(inputs=[catalog.checkbox, catalog.slider])
def display_values(checkbox: bool, slider: int) -> None:
    print(f"Checkbox is {checkbox}")
    print(f"Slider value is {slider}")
