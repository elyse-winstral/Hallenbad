import polars as pl
import datetime as dt
import numpy as np


#Make Time column a datetime variable and add weekday column
def read_in(df):
    df = df.with_columns(pl.col("Time").str.to_datetime("%a %d-%m-%Y %H:%M", exact=True))
    df = df.with_columns(pl.col("Time").dt.weekday().alias("Weekday")) # 1 = Monday, 7 = Sunday
    return df




#Replace all zeros in open hours with NaN, leave zeros outside of open hours 0
#Hours: mon:6-20, tue: 6-20, Wed:6-22, Thu: 6-20, Fri:6-22, Sat:6-22, Sun:6-22
def identify_missing_data (df):
    df = df.with_columns(Occupancy = pl.when((pl.col("Weekday").is_in([1, 2, 4])) & 
                                          (pl.col("Time").dt.hour().is_between(6,20, closed = "left")) & 
                                          (pl.col("Occupancy") == 0)).
                    then(np.nan).
                    otherwise(pl.col("Occupancy")))

    df = df.with_columns(Occupancy = pl.when((pl.col("Weekday").is_in([3, 5, 6, 7])) & 
                                          (pl.col("Time").dt.hour().is_between(6,22, closed = "left")) & 
                                          (pl.col("Occupancy") == 0)).
                    then(np.nan).
                    otherwise(pl.col("Occupancy")))
    return df


df = pl.read_csv("results.csv")

df = read_in(df)
#Drop entries before 2024-11-06
start_date = dt.datetime(2024, 11, 6, 5)
df = df.filter(pl.col("Time") > start_date)

df = identify_missing_data(df)
