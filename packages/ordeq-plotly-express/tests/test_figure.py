import plotly.express as px
from ordeq_plotly_express import PlotlyExpressFigure


def test_save_html(tmp_path):
    fig = px.scatter(x=[1, 2, 3], y=[4, 5, 6])
    out = PlotlyExpressFigure(path=tmp_path / "scatter.html")
    out.save(fig)
    assert (tmp_path / "scatter.html").exists()


def test_save_png(tmp_path):
    fig = px.scatter(x=[1, 2, 3], y=[4, 5, 6])
    out = PlotlyExpressFigure(path=tmp_path / "scatter.png")
    out.save(fig)
    assert (tmp_path / "scatter.png").exists()
