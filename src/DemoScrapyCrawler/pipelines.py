# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
from scrapy.exceptions import DropItem
class DemoscrapycrawlerPipeline(object):
    def __init__(self):
        self.ids_seen=set()
    def process_item(self, item, spider):
        if item['pageurl'] in self.ids_seen:
            raise DropItem ("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['pageUrl'])
            return item
