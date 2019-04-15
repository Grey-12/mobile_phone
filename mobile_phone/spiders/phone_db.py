# -*- coding: utf-8 -*-
import scrapy
import  re

from mobile_phone.items import PhoneDbItem


class PhoneDbSpider(scrapy.Spider):
    name = 'phone_db'
    allowed_domains = ['phoneDb.net']
    start_urls = []
    tmp_url = "http://phonedb.net/index.php?m=device&id={}"
    for i in range(1, 14945):
        url = tmp_url.format(i)
        start_urls.append(url)
    ref = re.compile(r"&id=(\d+)")
    # def parse(self, response):
    #     for i in range(1, 14945):
    #         url = self.tmp_url.format(i)
    #         yield scrapy.Request(url=url, callback=self.parse_detail, meta={"id": i})

    def parse(self, response):
        item = PhoneDbItem()
        item["id"] = re.search(self.ref, response.url).group(1)
        item["brand"] = ""
        if response.xpath('//a[@id="datasheet_item_id1"]/following-sibling::a/text()'):
            item["brand"] = response.xpath('//a[@id="datasheet_item_id1"]/following-sibling::a/text()').extract_first()
        item["model"] = ""
        if response.xpath('//a[@id="datasheet_item_id2"]/parent::td/text()'):
            item["model"] = response.xpath('//a[@id="datasheet_item_id2"]/parent::td/text()').extract_first()
        item["category"] = ""
        if response.xpath('//a[@id="datasheet_item_id28"]/following-sibling::a/text()'):
            item["category"] = response.xpath(
                '//a[@id="datasheet_item_id28"]/following-sibling::a/text()').extract_first()
        item["platform"] = ""
        if response.xpath('//a[@id="datasheet_item_id39"]/following-sibling::a/text()'):
            item["platform"] = response.xpath(
                '//a[@id="datasheet_item_id39"]/following-sibling::a/text()').extract_first()
        item["os"] = ""
        if response.xpath('//a[@id="datasheet_item_id32"]/following-sibling::a/text()'):
            item["os"] = response.xpath('//a[@id="datasheet_item_id32"]/following-sibling::a/text()').extract_first()
        item["codename"] = ""
        if response.xpath('//a[@id="datasheet_item_id6"]/following-sibling::a/text()'):
            item["codename"] = response.xpath(
                '//a[@id="datasheet_item_id6"]/following-sibling::a/text()').extract_first()
        yield item
