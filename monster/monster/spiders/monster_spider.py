# -*- coding: utf-8 -*-
import scrapy


class MonsterSpiderSpider(scrapy.Spider):
    name = "monster-spider"
    allowed_domains = ["monster.com"]
    start_urls = (
        'http://www.monster.com/',
    )

    def parse(self, response):
        pass
