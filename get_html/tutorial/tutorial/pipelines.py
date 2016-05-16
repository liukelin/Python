# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 定义项目管道   settings BOT_NAME
class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item

