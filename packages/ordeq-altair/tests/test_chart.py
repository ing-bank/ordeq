import altair as alt
import pandas as pd
import pytest
from ordeq_altair.chart import AltairChart


def test_chart(tmp_path):
    # Create a simple Altair chart
    source = pd.DataFrame({
        "a": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
        "b": [28, 55, 43, 91, 81, 53, 19, 87, 52],
    })

    chart = alt.Chart(source).mark_bar().encode(x="a", y="b")
    out_path = tmp_path / "chart.png"
    figure = AltairChart(path=out_path)
    figure.save(chart)
    assert out_path.exists()
    assert out_path.read_bytes().startswith(b"\x89PNG\r\n")


def test_chart_invalid_extension(tmp_path):
    invalid_path = tmp_path / "chart.txt"
    with pytest.raises(ValueError, match="Path extension must be one of"):
        AltairChart(path=invalid_path)
