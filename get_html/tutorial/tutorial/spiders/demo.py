#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: liukelin  314566990@qq.com
# 抓取网页
#

import scrapy

from tutorial.items import DemoItem

class demoSpider(scrapy.spiders.Spider):

    # scrapy crawl demo
    name = "demo"
    allowed_domains = ["fashionshootexperience.wordpress.com"]
    start_urls = [
        "https://fashionshootexperience.wordpress.com/2015/01/07/creepy-fairytale-with-broncolor/",
        "https://fashionshootexperience.wordpress.com/2016/02/21/ny-france-published/",
        "https://fashionshootexperience.wordpress.com/2016/01/07/rags-riches/",
        "https://fashionshootexperience.wordpress.com/2015/10/20/fashion-lanzarote/",
        "https://fashionshootexperience.wordpress.com/2015/10/15/lisa-griffin-award/",
        "https://fashionshootexperience.wordpress.com/2015/05/24/cross-century-couture-in-a-magical-fine-art-shoot-at-belvoir-castle/",
        "https://fashionshootexperience.wordpress.com/2015/04/03/miss-aniela-feature-in-normal-magazine/",
        "https://fashionshootexperience.wordpress.com/2015/01/07/creepy-fairytale-with-broncolor/",
        "https://fashionshootexperience.wordpress.com/2014/12/14/andrew-sars-in-miroir/",
        "https://fashionshootexperience.wordpress.com/2014/12/03/showcase-from-3-countries/",
        "https://fashionshootexperience.wordpress.com/2014/07/29/iceland-november-2014/",
        "https://fashionshootexperience.wordpress.com/2014/07/02/two-published-stories/",
        "https://fashionshootexperience.wordpress.com/2014/06/14/arctic-eye-candy/",
        "https://fashionshootexperience.wordpress.com/2014/01/15/phlearn/",
        "https://fashionshootexperience.wordpress.com/2014/01/08/episode-5-of-framed-the-photographer-me/",
        "https://fashionshootexperience.wordpress.com/2013/11/20/fetish-for-futuristic/",
        "https://fashionshootexperience.wordpress.com/2013/11/13/episode-4-of-framed-the-model/",
        "https://fashionshootexperience.wordpress.com/2013/11/02/episode-3-of-framed-the-make-up-artist/",
        "https://fashionshootexperience.wordpress.com/2013/10/28/episode-2-of-framed-the-stylist/",
        "https://fashionshootexperience.wordpress.com/2013/10/26/that-red-dress/",
        "https://fashionshootexperience.wordpress.com/2013/10/24/episode-1-of-framed-the-producer/",
        "https://fashionshootexperience.wordpress.com/2013/10/15/trailer-for-episode-1-of-fashion-shoot-experience-on-framed/",
        "https://fashionshootexperience.wordpress.com/2013/09/19/la-moodboard/",
        "https://fashionshootexperience.wordpress.com/2013/09/11/learn-about-you/",
        "https://fashionshootexperience.wordpress.com/2013/09/10/first-framed-episode/",
        "https://fashionshootexperience.wordpress.com/2013/09/10/ny-deliciousness/",

    ]

    def parse(self, response):
        
        #filename = response.url.split("/")[-2]
        #with open(filename, 'wb') as f:
        #    f.write(response.body) # 网页内容
        
        # image_path = '/Volumes/Liukelin/photos/fashionshootexperience.wordpress.com'

        # st = scrapy.selector(response=response).xpath('//img[@class="alignnone"]').extract()
        st = response.selector.xpath('//img/@src').extract() # 获取所有 img标签的 src属性  .re(r'[^/]*.[jpg|png|gif]$')
        # print "==%s==" % st
        # for img in st:
        #     image_path_name = "%s/%s" % (image_path, img.split("/")[-2])
        
        item = DemoItem() #实例化我们自己定义item，可以理解为实例化字典
        item['image_urls'] = st    # url
        item['images'] = response.selector.xpath('//img/@src').re(r'[^/]*.[jpg|png|gif]$') # 保存图片   
        return item   
