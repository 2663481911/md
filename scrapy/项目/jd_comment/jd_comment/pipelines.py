# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient

class JdCommentPipeline(object):
    
    
    def open_spider(self, spider):
        self.client = MongoClient(host='localhost', port=27017)
        self.db = self.client['scrapy_data']['jd_comment']
        
    def close_spider(self, spider):
        self.client.close()
    
    def process_item(self, item, spider):
        print(item)
        self.db.insert_one(item)
        return item
