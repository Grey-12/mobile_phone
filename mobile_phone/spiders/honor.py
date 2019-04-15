# -*- coding: utf-8 -*-
import scrapy

from mobile_phone.items import MobilePhoneItem


class HonorSpider(scrapy.Spider):
    name = 'honor'
    allowed_domains = ['www.mobilephonesspecs.com']
    start_urls = ['https://www.mobilephonesspecs.com/']
    temp_url = 'http://www.mobilephonesspecs.com/{}/page/{}'
    page = 1

    def parse(self, response):
        for li in response.xpath('//aside[@id="categories-3"]/ul//li'):
            url = li.xpath('./a/@href').extract_first()
            brand = li.xpath('./a/text()').extract_first()
            if brand != 'other':
                yield scrapy.Request(url=url,
                                     callback=self.parse_item,
                                     meta={'brand': brand})

    def parse_item(self, response):
        brand = response.meta['brand']
        urls = response.xpath('//div[@class="entry clearfix"]//a/@href').extract()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_detail, dont_filter=True,
                                 meta={'brand': brand})
        next_url = response.xpath('//a[@class="next page-numbers"]')

        if next_url:
            self.page += 1
            # 构造翻页请求
            yield response.follow(
                url=next_url.xpath('./@href').extract_first(),
                callback=self.parse_item,
                dont_filter=True,
                meta={'brand': brand}
            )

    def parse_detail(self, response):
        brand = response.meta['brand']
        item = MobilePhoneItem()
        tr = response.xpath('//td[contains(text(), "OS")]//../following-sibling::td[1]/text()').extract_first()
        item["category"] = tr
        item['model'] = response.xpath('//h1[@class="entry-title post-title"]/text()').extract_first()
        item["brand"] = brand
        print(item)
        yield item
