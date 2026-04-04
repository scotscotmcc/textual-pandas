import pytest

from textual.app import App
from textual.coordinate import Coordinate
from textual_pandas.widgets import DataFrameTable
import pandas as pd


df = pd.DataFrame()
df["Name"] = ["Dan", "Ben", "Don", "John", "Jim", "Harry"]
df["Score"] = [77, 56, 90, 99, 83, 69]
df["Grade"] = ["C", "F", "A", "A", "B", "D"]


class ClassApp(App):
    def compose(self):
        yield DataFrameTable()

    def on_mount(self):
        table = self.query_one(DataFrameTable)
        table.add_df(df)

@pytest.mark.asyncio
async def test_dataframetable():
    app = ClassApp()
    async with app.run_test() as pilot:
        dft = app.query_exactly_one(DataFrameTable)
        assert dft is not None
        assert len(dft.columns) == 3
        assert len(dft.rows) == 6
        assert dft.get_cell_at(Coordinate(0,0)) == 'Dan'
        assert dft.get_cell_at(Coordinate(1,1)) == 56
        assert dft.get_cell_at(Coordinate(2,2)) == "A"