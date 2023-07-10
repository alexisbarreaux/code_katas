import pandas as pd

from code_kata.data_munging.common import (
    get_columns_absolute_difference,
    get_row_for_smallest_value,
    load_data_as_dataframe,
)
from code_kata.data_munging.constants import WEATHER_FILENAME


def post_process_weather_dataframe(weather_df: pd.DataFrame) -> pd.DataFrame:
    """
    Specific processing for faulty characters
    """
    return weather_df.replace("\*", "", regex=True)


if __name__ == "__main__":
    df = load_data_as_dataframe(filename=WEATHER_FILENAME)
    df = post_process_weather_dataframe(weather_df=df)
    temperatures_spread = get_columns_absolute_difference(
        df=df, first_column_name="MxT", second_column_name="MnT"
    )
    row = get_row_for_smallest_value(df, temperatures_spread)
    print(row["Dy"])
