from requests_html import HTMLSession

session = HTMLSession()

# r= session.get('https://books.toscrape.com/')
r = session.get('https://www.flashscore.com/')
# r= session.get('https://www.youtube.com/')
# r= session.get('https://twitter.com/home')
# r= session.get('https://support.twitter.com/articles/20170514')

# print(r.html.find('.event'))
print(r.html.title)
# for data in r.html.find('a'):
    # print(data)
# print(r.html.find('.price_color'))