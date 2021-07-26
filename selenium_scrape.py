# import selenium
# from selenium import webdriver
# from selenium.common.exceptions import ElementClickInterceptedException

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

url = 'https://books.toscrape.com/'
driver = webdriver.Chrome('/home/marvin/chromedriver')
driver.get(url)
