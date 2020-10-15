import scrapy
from quotes.items import QuotesItem
from scrapy.loader import ItemLoader

class QuotesSpiderSpider(scrapy.Spider):
    name = 'quotes_spider'
    allowed_domains = ['quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com//']

    def parse(self, response):
        quotes = response.css("div.quote")
        
        for quote in quotes:
            
            loader = ItemLoader(item = QuotesItem(),selector = quote)
            loader.add_css("author",".author::text")
            loader.add_css("quote",".text::text")
            loader.add_css("tags",".tag::text")
            
            yield loader.load_item()