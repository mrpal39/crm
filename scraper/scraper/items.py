# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

import pathlib


class BlogItem(scrapy.Item):
    title = scrapy.Field()
    detail = scrapy.Field()

class QuotesItem(scrapy.Item):
    author = scrapy.Field()
    text = scrapy.Field()
