from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime 
import pandas as pd

driver = webdriver.Firefox()
driver.implicitly_wait(5)

URL = "https://www.stadt-zuerich.ch/de/stadtleben/sport-und-erholung/sport-und-badeanlagen/hallenbaeder/oerlikon.html"
driver.get(URL)

nums = driver.find_element(By.ID, "SSD-7")
occupancy = nums.text
occupancy = int(occupancy)
driver.quit()


header = ["Time", "Occupancy"]

now = datetime.now()
date = now.strftime("%a %d-%m-%Y %H:%M")
data = [date, occupancy]

df = pd.read_csv("results.csv")
df = pd.concat([df, pd.DataFrame([data], columns = header)], ignore_index=True)
df.to_csv("results.csv",index=False)