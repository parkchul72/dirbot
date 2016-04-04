# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from scrapy.selector import Selector

from dirbot.items import NaverWebsite


class NaverItSpider(Spider):
    name = "naverit"
    allowed_domains = ["naver.com"]
    start_urls = [
        "http://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=105&listType=title&date="
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html
        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """

        sel = Selector(response)
        sites = sel.xpath('//ul[@class="type02"]/li')
        items = []

        for site in sites:
            item = NaverWebsite()
            item['name'] = site.xpath('a/text()').extract()
            item['url'] = site.xpath('a/@href').extract()
            item['creator'] = site.xpath('span[@class="writing"]/text()').extract()
            item['date'] = site.xpath('span[@class="date"]/text()').extract()
            items.append(item)

        return items