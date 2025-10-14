import pandas as pd
from ordeq_pandas import PandasDataFrame


def test_it_loads():
    data = [
        (2022, "file_2022.xlsx"),
        (2023, "file_2023.xlsx"),
        (2024, "file_2024.xlsx"),
    ]
    columns = ["year", "datafile"]
    expected = pd.DataFrame(data, columns=columns)
    actual = PandasDataFrame(data=data, columns=columns).load()
    pd.testing.assert_frame_equal(actual, expected)
