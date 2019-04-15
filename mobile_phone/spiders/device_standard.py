# -*- coding: utf-8 -*-
import scrapy

from mobile_phone.items import DeviceItem


class DeviceStandardSpider(scrapy.Spider):
    name = 'device_standard'
    allowed_domains = ['devicespecifications.com']
    start_urls = ['http://devicespecifications.com/en/brand-more']
    title_url = "www.devicespecifications.com/en/brand"

    def parse(self, response):
        urls = response.xpath('//div[@class="brand-listing-container-news"]/a/@href').extract()
        for url in urls:
            url = str(url)
            yield scrapy.Request(url=url, callback=self.parse_item)

    def parse_item(self, response):
        detail_urls = response.xpath('//div[@class="model-listing-container-80"]//h3/a/@href').extract()
        for detail_url in detail_urls:
            yield scrapy.Request(url=detail_url, callback=self.parse_detail)

    def parse_detail(self, response):
        item = DeviceItem()
        item["brand"] = ""
        if response.xpath('//td[contains(text(), "Brand")]/following-sibling::td/text()'):
            item["brand"] = response.xpath(
                '//td[contains(text(), "Brand")]/following-sibling::td/text()').extract_first()
        item["model"] = ""
        if response.xpath('//p[contains(text(), "Model name of the device.")]/../following-sibling::td/text()'):
            item["model"] = response.xpath(
                '//p[contains(text(), "Model name of the device.")]/../following-sibling::td/text()').extract_first()
        item["model_alias"] = ""
        if response.xpath('//td[contains(text(), "Model alias")]/following-sibling::td/text()'):
            item["model_alias"] = response.xpath(
                '//td[contains(text(), "Model alias")]/following-sibling::td/text()').extract()
        item["os"] = ""
        if response.xpath('//td[contains(text(), "Operating system (OS)")]/following-sibling::td/text()'):
            item["os"] = response.xpath(
                '//td[contains(text(), "Operating system (OS)")]/following-sibling::td/text()').extract_first()
        yield item
