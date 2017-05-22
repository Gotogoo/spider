# -*- coding: utf-8 -*-

import scrapy

class CnblogsItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    date = scrapy.Field()
    view =  scrapy.Field()
