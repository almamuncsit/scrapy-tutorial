import scrapy
from ..items import QuotestutorialItem


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com'
    ]

    def parse(self, response):
        item = QuotestutorialItem()

        all_div_quotes = response.css('div.quote')

        for quote in all_div_quotes:
            item['title'] = quote.css('span.text::text').extract()
            item['author'] = quote.css('.author::text').extract()
            item['tags'] = quote.css('.tag::text').extract()

            yield item

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
