# -*- coding: utf-8 -*-

# Define here the models for your scraped items
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class TechcrawlersItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    writtennews = scrapy.Field()
    autor = scrapy.Field()
    editor = scrapy.Field()
    tags = scrapy.Field()
    hora = scrapy.Field()
    url = scrapy.Field()
    website = scrapy.Field()
    paragraphsnumber = scrapy.Field()