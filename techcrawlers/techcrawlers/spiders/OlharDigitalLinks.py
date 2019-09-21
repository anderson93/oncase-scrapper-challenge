import os
import datetime
from bs4 import BeautifulSoup                                                                                                                 
import scrapy

class OlharDigitalLinksScrapper(scrapy.Spider):
    name = "olhardigital-links"

    allowed_domains = ['olhardigital.com.br']
 
    def start_requests(self):
        urls = [f'https://olhardigital.com.br/noticias/{page}' for page in range(1,100)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        news = response.css("div.blk-items")[0] 
        urls = news.css("a::attr(href)").getall()
        for url in urls:
            yield {
                    'url':'http:'+url
                    }