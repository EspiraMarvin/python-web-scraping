from urllib.request import urlopen
from bs4 import BeautifulSoup

url_to_scrape = "https://books.toscrape.com/"
request_page = urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')

 # get book title
for data in html_soup.select('ol'):
    for a in data.find_all('a'):
        print(a.get_text())

 # get book prices
for price in html_soup.find_all("p", class_="price_color"):
    print(price.get_text())

