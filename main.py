from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep
import scraping_bot

driver = webdriver.Chrome()
driver.maximize_window()

url = "https://www.ucsfdentalcenter.org/"
driver.get(url)


homecards = driver.find_elements(By.TAG_NAME, "main")
print(len(homecards))
print(homecards[0].text)
