import pandas as pd
import numpy as np


df = pd.read_csv("results.csv")

#used to filter out first 16 values- reason: experimental values
#df = df.iloc[16:].reset_index()


zeros = (df["Occupancy"] == 0).sum()
print("portion of zeros ", zeros / df.shape[0]) # approx 32% as of 30/11/24


#Replace all zeros in open hours with NaN, leave zeros outside of open hours 0
#Hours: mon:6-20, tue: 6-20, Wed:6-22, Thu: 6-20, Fri:6-22, Sat:6-22, Sun:6-22

df.loc[(df["Time"].str[0:3].isin(["Mon", "Tue", "Thu"])) & 
       (df['Time'].str[-5:] >= "06:00") &  
       (df['Time'].str[-5:] <= "20:00") & 
       (df["Occupancy"] == 0), "Occupancy"] = np.nan

df.loc[(df["Time"].str[0:3].isin(["Wed", "Fri", "Sat", "Sun"])) & 
       (df['Time'].str[-5:] >= "06:00") &  
       (df['Time'].str[-5:] <= "22:00") & 
       (df["Occupancy"] == 0), "Occupancy"] = np.nan

new_zeros = (df["Occupancy"] == 0).sum()
print("Updated: portion of zeros ", new_zeros/df.shape[0]) #arppox. 6% as of 30/11/24 
