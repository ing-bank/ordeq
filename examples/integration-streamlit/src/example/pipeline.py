import catalog
from ordeq import node


@node(inputs=[catalog.checkbox, catalog.slider])
def display_values(checkbox: bool, slider: int) -> None:
    """Displays the values of the checkbox and slider.

    Args:
        checkbox: The value of the checkbox.
        slider: The value of the slider.

    """

    print(f"Checkbox is {checkbox}")
    print(f"Slider value is {slider}")
