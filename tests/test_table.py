import pytest

from textual.app import App
from textual.coordinate import Coordinate
from textual_pandas.widgets import DataFrameTable
import pandas as pd


@pytest.mark.asyncio
async def test_dataframetable():
    "asdf"
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

    app = ClassApp()
    async with app.run_test() as pilot:
        dft = app.query_exactly_one(DataFrameTable)
        assert dft is not None
        assert len(dft.columns) == 3
        assert len(dft.rows) == 6
        assert dft.get_cell_at(Coordinate(0, 0)) == "Dan"
        assert dft.get_cell_at(Coordinate(1, 1)) == 56
        assert dft.get_cell_at(Coordinate(2, 2)) == "A"
        df.insert(
            1,
            "Teacher",
            [
                "Mr. Smith",
                "Mr. Smith",
                "Mr. Smith",
                "Mr. Smith",
                "Mr. Smith",
                "Mr. Smith",
            ],
        )
        dft.update_df(df)
        assert dft is not None
        assert len(dft.columns) == 4
        assert len(dft.rows) == 6
        assert dft.get_cell_at(Coordinate(0, 0)) == "Dan"
        assert dft.get_cell_at(Coordinate(1, 1)) == "Mr. Smith"
        assert dft.get_cell_at(Coordinate(2, 2)) == 90
        assert dft.get_cell_at(Coordinate(3, 3)) == "A"
