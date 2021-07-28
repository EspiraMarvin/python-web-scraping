from requests_html import HTMLSession
session = HTMLSession()

r= session.get('https://books.toscrape.com/')
get_books = r.html.find('.row')[2]

# get book title
for title in get_books.find('h3'):
    print(title.text)

# get book prices
for price in get_books.find('.price_color'):
    print(price.text)
