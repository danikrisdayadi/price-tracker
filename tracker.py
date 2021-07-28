from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://shopee.sg/HYDRAULIC-MONITOR-MOUNTING-ARM-NB-F80-LCD-SCREEN-DESK-TABLE-VESA-MOUNT-STAND-360-ADJUSTABLE-ROTATION-i.13842071.2689454006"
headers = headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36" }
driver = webdriver.Chrome("C:\\Users\\kanis\\Documents\\Legit Stuff\\NUS\\YSI SEA\\Java Extras\\chromedriver_win32\\chromedriver.exe")
driver.get(url)

title_name = driver.find_element_by_xpath("//span[contains(text(), 'VESA MOUNT')]")
product = driver.find_element_by_xpath("//button[contains(text(), 'F80')]")
product.click()
price = driver.find_element_by_xpath("//div[@class='_3e_UQT']")