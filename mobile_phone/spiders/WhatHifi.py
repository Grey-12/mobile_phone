# -*- coding: utf-8 -*-
import scrapy

from mobile_phone.items import WhatHifiItem


class WhathifiSpider(scrapy.Spider):
    name = 'WhatHifi'
    allowed_domains = ['www.whathifi.com']
    start_urls = ['http://www.whathifi.com/brands']
    key_word = ["brand", "title"]

    def parse(self, response):

        for url in response.xpath('//section/ul/li/a'):
            brand = url.xpath('./text()').extract_first()
            brand_url = url.xpath('./@href').extract_first()

            yield scrapy.Request(url=brand_url, callback=self.parse_item, meta={"brand": brand})

    def parse_item(self, response):
        brand = response.meta["brand"]
        # current_url = response.url
        for res in response.xpath('//div[@class="listingResults"]/div'):
            detail_url = res.xpath('./a/@href').extract_first()
            title = res.xpath('.//h3/text()').extract_first()

            yield scrapy.Request(url=detail_url, callback=self.parse_detail, meta={"brand": brand, "title": title})

        next_url = response.xpath('//span[@class="product_pagination__forward"]/a[contains(text(), "Next ›")]')
        # //span[@class='product_pagination__forward']/a[contains(text(), "Next ›")]/@href
        if next_url:
            # self.page += 1
            # 构造翻页请求
            yield scrapy.Request(
                url=next_url.xpath('./@href').extract_first(),
                callback=self.parse_item,
                # dont_filter=True,
                meta={'brand': brand}
            )

    def parse_detail(self, response):
        brand = response.meta["brand"]
        title = response.meta["title"]
        item = WhatHifiItem()
        item = {item[i]: "" for i in self.key_word}
        item["brand"] = brand
        item["title"] = title




