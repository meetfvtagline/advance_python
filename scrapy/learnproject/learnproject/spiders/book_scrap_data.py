import scrapy

class BookScrapDataSpider(scrapy.Spider):
    '''Spider to scrape book data from Bookswagon best seller page'''

    name='book_scrap_data'
    start_urls=['https://www.bookswagon.com/promo-best-seller/books-best-books-of-the-year/91579C57AD0D']
    def parse(self,response):
        books=response.css('div.card')
        for book in books:
            yield{
                'title':book.css('span.booktitle::text').get(default="").strip(),
                'author':book.css('span.author::text').get(default="").strip(),
                'actual_price':book.css('span.actualprice::text').get(default="").strip(),
            }
    
        # next_page=response.css('.next a::attr(href)').get()
        # if next_page:
        #     yield response.follow(next_page,callback=self.parse)

