from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
url = 'https://books.toscrape.com/'

# path to the chromedriver
driver = webdriver.Chrome('/home/marvin/chromedriver')
driver.get(url)

def get_books_info():
    data = []
    container = driver.find_element_by_xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol')

    titles = container.find_elements(By.TAG_NAME, 'a')
    for title in titles:
        print(title.text)

    prices = container.find_elements(By.CLASS_NAME, 'price_color')
    for price in prices:
        print(price.text)

    next_page = driver.find_element_by_link_text('next')
    next_page.click()


for x in range(5):
    get_books_info()
driver.quit()