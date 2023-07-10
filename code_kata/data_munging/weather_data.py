import numpy as np
import pandas as pd

from code_kata.data_munging.constants import DATA_FOLDER_PATH, WEATHER_FILENAME


def process_weather_data():
    with open(DATA_FOLDER_PATH / WEATHER_FILENAME, "r") as file:
        df = pd.read_fwf(file)

    # Remove faulty characters
    df.replace("\*", "", inplace=True, regex=True)

    temperature_spread = df["MxT"].astype(float) - df["MnT"].astype(float)
    smallest_spread_index = np.argmin(temperature_spread)

    return df.loc[smallest_spread_index]["Dy"]
