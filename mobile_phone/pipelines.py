# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class MobilePhonePipeline(object):
    def process_item(self, item, spider):
        with open("tmp.json", "a") as f:
            # json.dump(dict(item),f)
            f.write(json.dumps(dict(item)) + "\n")


class PhoneWorldPipeline(object):
    def process_item(self, item, spider):
        with open("phone_world.json", "a", encoding="utf-8") as f:
            f.write(json.dumps(dict(item), ensure_ascii=False) + "\n")


class PhoneDBPipeline(object):
    def process_item(self, item, spider):
        with open("Phone_DB.json", "a", encoding="utf-8") as f:
            f.write(json.dumps(dict(item), ensure_ascii=False) + "\n")


class DeviceStandardPipeline(object):
    def process_item(self, item, spider):
        with open("device_standard.json", "a", encoding="utf-8") as f:
            f.write(json.dumps(dict(item), ensure_ascii=False) + "\n")


class MyPhonePipeline(object):
    def process_item(self, item, spider):
        with open("my_phone.json", "a", encoding="utf-8") as f:
            f.write(json.dumps(dict(item), ensure_ascii=False) + "\n")
