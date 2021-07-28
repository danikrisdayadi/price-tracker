from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from datetime import date
import csv

url = "https://shopee.sg/HYDRAULIC-MONITOR-MOUNTING-ARM-NB-F80-LCD-SCREEN-DESK-TABLE-VESA-MOUNT-STAND-360-ADJUSTABLE-ROTATION-i.13842071.2689454006"
headers = headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36" }
driver = webdriver.Chrome("C:\\Users\\kanis\\Documents\\Legit Stuff\\NUS\\YSI SEA\\Java Extras\\chromedriver_win32\\chromedriver.exe")
driver.get(url)

timeout = 3 # seconds
try:
    myElem = WebDriverWait(driver, timeout).until(expected_conditions.presence_of_element_located((By.XPATH, "//span[contains(text(), 'VESA MOUNT')]")))
except TimeoutException:
    print ("Loading took too much time!")

title_name = driver.find_element_by_xpath("//span[contains(text(), 'VESA MOUNT')]")
product = driver.find_element_by_xpath("//button[contains(text(), 'F80')]")
product.click()
price = driver.find_element_by_xpath("//div[@class='_3e_UQT']")

price_list = [date.today(), title_name.text, price.text]

with open('./price_history.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(price_list)

driver.close()