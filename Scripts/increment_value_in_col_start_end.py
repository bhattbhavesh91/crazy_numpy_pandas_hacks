import numpy as np
import pandas as pd
from pandas import Timestamp

data = [
    {"Date": Timestamp("2001-01-01 00:00:00"), "Stock_Value": 10, "Start_End": "Start"},
    {"Date": Timestamp("2001-01-02 00:00:00"), "Stock_Value": 20, "Start_End": np.nan},
    {"Date": Timestamp("2001-01-03 00:00:00"), "Stock_Value": 30, "Start_End": np.nan},
    {"Date": Timestamp("2001-01-04 00:00:00"), "Stock_Value": 50, "Start_End": np.nan},
    {"Date": Timestamp("2001-01-05 00:00:00"), "Stock_Value": 60, "Start_End": np.nan},
    {"Date": Timestamp("2001-01-06 00:00:00"), "Stock_Value": 54, "Start_End": "End"},
    {"Date": Timestamp("2001-01-07 00:00:00"), "Stock_Value": 11, "Start_End": "Start"},
    {"Date": Timestamp("2001-01-08 00:00:00"), "Stock_Value": 12, "Start_End": np.nan},
    {"Date": Timestamp("2001-01-09 00:00:00"), "Stock_Value": 13, "Start_End": np.nan},
    {"Date": Timestamp("2001-01-10 00:00:00"), "Stock_Value": 14, "Start_End": np.nan},
    {"Date": Timestamp("2001-01-11 00:00:00"), "Stock_Value": 15, "Start_End": np.nan},
    {"Date": Timestamp("2001-01-12 00:00:00"), "Stock_Value": 16, "Start_End": "End"},
    {"Date": Timestamp("2001-01-13 00:00:00"), "Stock_Value": 76, "Start_End": "Start"},
    {"Date": Timestamp("2001-01-14 00:00:00"), "Stock_Value": 80, "Start_End": np.nan},
    {"Date": Timestamp("2001-01-15 00:00:00"), "Stock_Value": 81, "Start_End": np.nan},
    {"Date": Timestamp("2001-01-16 00:00:00"), "Stock_Value": 91, "Start_End": np.nan},
    {"Date": Timestamp("2001-01-17 00:00:00"), "Stock_Value": 111, "Start_End": np.nan},
    {"Date": Timestamp("2001-01-18 00:00:00"), "Stock_Value": 112, "Start_End": np.nan},
    {"Date": Timestamp("2001-01-19 00:00:00"), "Stock_Value": 121, "Start_End": np.nan},
    {"Date": Timestamp("2001-01-20 00:00:00"), "Stock_Value": 154, "Start_End": "End"},
]

df = pd.DataFrame(data)
print(df.head())

df["Row_values"] = 0
for i in range(df.shape[0]):
    if pd.isnull(df.loc[i, "Start_End"]):
        df.loc[i, "Row_values"] = df.loc[i - 1, "Row_values"] + 1
    elif df.loc[i, "Start_End"] == "End":
        df.loc[i, "Row_values"] = df.loc[i - 1, "Row_values"] + 1

print(df)
