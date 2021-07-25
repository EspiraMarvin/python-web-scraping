from requests_html import HTMLSession
session = HTMLSession()

r= session.get('https://books.toscrape.com/')
getBooks = r.html.find('.row')[2]

# get book title
for title in getBooks.find('h3'):
    print(title.text)

# get book prices
for price in getBooks.find('.price_color'):
    print(price.text)
