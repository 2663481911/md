# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

class KuwoMusicPipeline:
    def open_spider(self, spider):
        self.client = MongoClient(host='127.0.0.1', port=27017)
        self.db = self.client['scrapy_data']['jd_comment']

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # print(item)
        self.db.insert_one(item)
        return item


