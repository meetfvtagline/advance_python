import scrapy
from scrapy.crawler import CrawlerProcess

class MySpider(scrapy.Spider):
    name = "example"
    start_urls = [
        "https://quotes.toscrape.com/page/1/",
    ]

    def parse(self, response):
        # title = response.css("small.author::text").getall()
        # tags=response.css("div.tags a.tag::text").getall()
        # quo=response.css("div.quote")
        # print("Title:", title)
        # print("Tags:", tags)
        # print("Quotes:", quo) 
        for quote in response.css("div.quote"):
            yield { 
                "text": quote.css("span.text::text").get(),     
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("a.tag::text").getall()
            }
         

process = CrawlerProcess(settings={
    "LOG_LEVEL": "ERROR"
})

process.crawl(MySpider)
process.start()