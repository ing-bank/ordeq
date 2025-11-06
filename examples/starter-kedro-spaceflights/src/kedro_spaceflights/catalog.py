from pathlib import Path

from ordeq_pandas import PandasCSV, PandasExcel, PandasParquet

companies = PandasCSV(path=Path("data/01_raw/companies.csv"))

shuttles = PandasExcel(
    path=Path("data/01_raw/shuttles.xlsx")
).with_load_options(engine="openpyxl")

preprocessed_companies = PandasParquet(
    path=Path("data/02_intermediate/preprocessed_companies.parquet")
)

preprocessed_shuttles = PandasParquet(
    path=Path("data/02_intermediate/preprocessed_shuttles.parquet")
)
