# -*- coding: utf-8 -*-
import scrapy


class DemoscrapyspiderSpider(scrapy.Spider):
    name = 'DemoScrapySpider'
    allowed_domains = ['agl.com.au']
    start_urls = ['http://agl.com.au/']

    def parse(self, response):
        pass
