from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime 
import time
import pandas as pd

driver = webdriver.Firefox()
driver.implicitly_wait(5)

URL = "https://www.stadt-zuerich.ch/ssd/de/index/sport/schwimmen/hallenbaeder/hallenbad_oerlikon.html"
driver.get(URL)

nums = driver.find_element(By.ID, "SSD-7")
occupancy = nums.text
occupancy = int(occupancy)
driver.quit()


header = ["Time", "Occupancy"]

#UPDATE TIME PORTION OF CODE FOR STRF
date = str(time.localtime().tm_mday) + "/" + str(time.localtime().tm_mon) + "-" + str(time.localtime().tm_hour) + ":" + str(time.localtime().tm_min)
data = [date, occupancy]

df = pd.read_csv("results.csv")
df = pd.concat([df, pd.DataFrame([data], columns = header)], ignore_index=True)
df.to_csv("results.csv",index=False)

print("yo")