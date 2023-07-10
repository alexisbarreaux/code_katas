import numpy as np
import pandas as pd

from code_kata.data_munging.constants import DATA_FOLDER_PATH, FOOTBALL_FILENAME


def process_football_data():
    with open(DATA_FOLDER_PATH / FOOTBALL_FILENAME, "r") as file:
        df = pd.read_fwf(file)

    # Remove faulty characters
    df.replace("-", "", inplace=True, regex=True)
    columns = ["Match"] + df.columns[0].split()
    df = df[df.columns[0]].str.split("\s+", expand=True, regex=True)
    df.columns = columns

    scores_spread = np.abs(df["F"].astype(float) - df["A"].astype(float))
    smallest_spread_index = np.argmin(scores_spread)

    return df.loc[smallest_spread_index]["Team"]
