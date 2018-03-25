# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class TecentSpiderPipeline(object):
    def __init__(self):
        self.file_name = open("tecent.json", 'wb')

    def process_item(self, item, spider):
        json_text = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file_name.write(json_text.encode("utf-8"))
        return item

    def close_spider(self, spider):
        self.file_name.close()
