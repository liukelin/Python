# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DemoItem(scrapy.Item):
    # 我们定义的菜单，类似字典的形式
    image_urls = scrapy.item.Field()  # 定义图片url                          
    images = scrapy.item.Field()	  # 定义图片
