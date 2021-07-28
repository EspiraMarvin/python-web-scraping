import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = [
        'https://books.toscrape.com/'
    ]

    def parse(self, response):
        for book in response.css('div ol.row'):
            title = book.css('h3 a::text').getall()
            price = book.css('p.price_color::text').getall()
            yield {
                'title': book.css('h3 a::text').getall(),
                'price': book.css('p.price_color::text').getall()
            }
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

