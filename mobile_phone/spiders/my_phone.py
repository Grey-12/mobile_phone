# -*- coding: utf-8 -*-
import scrapy


class MyPhoneSpider(scrapy.Spider):
    name = 'my_phone'
    allowed_domains = ['https://whatismyphone.com/']
    start_urls = ['http://https://whatismyphone.com//']

    def parse(self, response):
        pass
