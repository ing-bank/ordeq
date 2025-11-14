import ibis
import polars as pl
import pytest
from ordeq_ibis import IbisView


@pytest.mark.parametrize("resource", ["polars://", "duckdb://"])
def test_it_saves(df: pl.DataFrame, resource: str):
    """Test that IbisView can save data as a view."""
    view_name = "test_view"
    view_io = IbisView(name=view_name, resource=resource)

    # Save the data as a view
    view_io.save(ibis.memtable(df))

    # Verify the view was created by accessing it through the backend
    backend = ibis.connect(resource)
    loaded_view = backend.table(view_name)
    assert loaded_view.to_polars().equals(df)
