# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MobilePhoneItem(scrapy.Item):
    # define the fields for your item here like:
    brand = scrapy.Field()
    model = scrapy.Field()
    category = scrapy.Field()


class PhoneWorldItem(scrapy.Item):
    brand = scrapy.Field()
    model = scrapy.Field()
    category = scrapy.Field()
    name = scrapy.Field()
    os = scrapy.Field()


class PhoneDbItem(scrapy.Item):
    id = scrapy.Field()
    brand = scrapy.Field()
    model = scrapy.Field()
    category = scrapy.Field()
    platform = scrapy.Field()
    os = scrapy.Field()
    codename = scrapy.Field()


class DeviceItem(scrapy.Item):
    brand = scrapy.Field()
    model = scrapy.Field()
    model_alias = scrapy.Field()
    os = scrapy.Field()


class MyPhoneItem(scrapy.Item):
    title = scrapy.Field()
    os = scrapy.Field()
    device_type = scrapy.Field()
    hardware_vendor = scrapy.Field()
    OEM = scrapy.Field()
    hardware_name = scrapy.Field()
