# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from douban.settings import mongo_host,mongo_port,mongo_name,mongo_connection

class ReptilePipeline(object):
    def process_item(self, item, spider):
        return item

class DoubanPipeline(object):
    def __init__(self):
        host=mongo_host
        port=mongo_port
        client = pymongo.MongoClient(host=host, port=port)
        db= client[mongo_name]
        self.post= db[mongo_connection]
    def process_item(self, item, spider):
        data= dict(item)
        self.post.insert(data)
        return item
