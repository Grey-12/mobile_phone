# -*- coding: utf-8 -*-
import scrapy
from mobile_phone.items import PhoneWorldItem
from urllib.parse import urljoin


class PhoneWorldSpider(scrapy.Spider):
    name = 'phone_world'
    allowed_domains = ['www.3533.com']
    start_urls = ['http://3533.com/phone']
    title_url = "www.3533.com"

    def parse(self, response):
        for a in response.xpath('//div[@class="box"]/ul/li/a'):
            brand = a.xpath('./img/@alt').extract_first()
            url = 'http://www.3533.com/' + a.xpath('./@href').extract_first()
            yield scrapy.Request(url=url, callback=self.parse_item, meta={"brand": brand})

    def parse_item(self, response):
        brand = response.meta["brand"]
        years_urls = response.xpath('//div[@class="year"]/ul/li/a')
        if years_urls:
            for a in years_urls:
                url = a.xpath('./@href').extract_first()
                yield response.follow(url=url, callback=self.parse_detail, meta={"brand": brand})
        else:
            phone_urls = response.xpath('//dd[@class="dd1"]//../preceding-sibling::dt[1]')
            for phone_url in phone_urls:
                phone_url = 'http://www.3533.com' + phone_url.xpath('./a/@href').extract_first() + 'canshu.htm'
                yield scrapy.Request(url=phone_url, callback=self.parse_specification, meta={"brand": brand},
                                     dont_filter=True)

    def parse_detail(self, response):
        brand = response.meta["brand"]
        phone_urls = response.xpath('//dd[@class="dd1"]//../preceding-sibling::dt[1]')
        for phone_url in phone_urls:

            phone_url = 'http://www.3533.com' + phone_url.xpath('./a/@href').extract_first() + 'canshu.htm'

            yield scrapy.Request(url=phone_url, callback=self.parse_specification,
                                 meta={"brand": brand},
                                 dont_filter=True)

    def parse_specification(self, response):
        item = PhoneWorldItem()
        tmp_li = response.url.split("/")
        item["brand"] = tmp_li[3]
        item["model"] = tmp_li[4].replace("_", " ")
        item["category"] = response.xpath(
            '//span[contains(text(), "系统界面：")]//../following-sibling::span[1]/text()').extract_first()
        item["name"] = response.xpath(
            '//span[contains(text(), "产品类型：")]//../following-sibling::span[1]/text()').extract_first()
        item["os"] = response.xpath(
            '//span[contains(text(), "操作系统：")]//../following-sibling::span[1]/text()').extract_first()
        # print(item)
        yield item
