import pandas as pd

from code_kata.data_munging.common import (
    get_columns_absolute_difference,
    get_row_for_smallest_value,
    load_data_as_dataframe,
)
from code_kata.data_munging.constants import FOOTBALL_FILENAME


def post_process_football_data(football_df: pd.DataFrame) -> pd.DataFrame:
    """
    Specific processing for faulty characters
    """
    football_df.replace("-", "", inplace=True, regex=True)
    columns = ["Match"] + football_df.columns[0].split()
    football_df = football_df[football_df.columns[0]].str.split(
        "\s+", expand=True, regex=True
    )
    football_df.columns = columns
    return football_df


if __name__ == "__main__":
    df = load_data_as_dataframe(filename=FOOTBALL_FILENAME)
    df = post_process_football_data(football_df=df)
    temperatures_spread = get_columns_absolute_difference(
        df=df, first_column_name="F", second_column_name="A"
    )
    row = get_row_for_smallest_value(df, temperatures_spread)
    print(row["Team"])
