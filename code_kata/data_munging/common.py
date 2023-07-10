import numpy as np
import pandas as pd

from code_kata.data_munging.constants import DATA_FOLDER_PATH


def load_data_as_dataframe(filename: str) -> pd.DataFrame:
    with open(DATA_FOLDER_PATH / filename, "r") as file:
        df = pd.read_fwf(file)
    return df


def get_columns_absolute_difference(
    df: pd.DataFrame, first_column_name: str, second_column_name: str
) -> np.ndarray:
    return np.abs(
        df[first_column_name].astype(float) - df[second_column_name].astype(float)
    )


def get_row_for_smallest_value(df: pd.DataFrame, values: np.ndarray) -> pd.DataFrame:
    smallest_index = np.argmin(values)
    return df.loc[smallest_index]
