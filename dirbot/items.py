# -*- coding: utf-8 -*-

from scrapy.item import Item, Field

class NaverWebsite(Item):
    name = Field()
    url = Field()
    creator = Field()
    date = Field()
