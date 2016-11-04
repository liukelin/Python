#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: liukelin  314566990@qq.com
# 抓取网页
#

import scrapy

from tutorial.items import DemoItem

class demoSpider(scrapy.spiders.Spider):

    # scrapy crawl demo 运行
    name = "demo"
    allowed_domains = ["jd.com"]
    start_urls = [
        # == Miss Aniela ==
        #fashionshootexperience.wordpress.com
        # "https://fashionshootexperience.wordpress.com/2015/01/07/creepy-fairytale-with-broncolor/",
        # "https://fashionshootexperience.wordpress.com/2016/02/21/ny-france-published/",
        # "https://fashionshootexperience.wordpress.com/2016/01/07/rags-riches/",
        # "https://fashionshootexperience.wordpress.com/2015/10/20/fashion-lanzarote/",
        # "https://fashionshootexperience.wordpress.com/2015/10/15/lisa-griffin-award/",
        # "https://fashionshootexperience.wordpress.com/2015/05/24/cross-century-couture-in-a-magical-fine-art-shoot-at-belvoir-castle/",
        # "https://fashionshootexperience.wordpress.com/2015/04/03/miss-aniela-feature-in-normal-magazine/",
        # "https://fashionshootexperience.wordpress.com/2015/01/07/creepy-fairytale-with-broncolor/",
        # "https://fashionshootexperience.wordpress.com/2014/12/14/andrew-sars-in-miroir/",
        # "https://fashionshootexperience.wordpress.com/2014/12/03/showcase-from-3-countries/",
        # "https://fashionshootexperience.wordpress.com/2014/07/29/iceland-november-2014/",
        # "https://fashionshootexperience.wordpress.com/2014/07/02/two-published-stories/",
        # "https://fashionshootexperience.wordpress.com/2014/06/14/arctic-eye-candy/",
        # "https://fashionshootexperience.wordpress.com/2014/01/15/phlearn/",
        # "https://fashionshootexperience.wordpress.com/2014/01/08/episode-5-of-framed-the-photographer-me/",
        # "https://fashionshootexperience.wordpress.com/2013/11/20/fetish-for-futuristic/",
        # "https://fashionshootexperience.wordpress.com/2013/11/13/episode-4-of-framed-the-model/",
        # "https://fashionshootexperience.wordpress.com/2013/11/02/episode-3-of-framed-the-make-up-artist/",
        # "https://fashionshootexperience.wordpress.com/2013/10/28/episode-2-of-framed-the-stylist/",
        # "https://fashionshootexperience.wordpress.com/2013/10/26/that-red-dress/",
        # "https://fashionshootexperience.wordpress.com/2013/10/24/episode-1-of-framed-the-producer/",
        # "https://fashionshootexperience.wordpress.com/2013/10/15/trailer-for-episode-1-of-fashion-shoot-experience-on-framed/",
        # "https://fashionshootexperience.wordpress.com/2013/09/19/la-moodboard/",
        # "https://fashionshootexperience.wordpress.com/2013/09/11/learn-about-you/",
        # "https://fashionshootexperience.wordpress.com/2013/09/10/first-framed-episode/",
        # "https://fashionshootexperience.wordpress.com/2013/09/10/ny-deliciousness/",


        # # rockstarlavender.wordpress.com
        # 'https://rockstarlavender.wordpress.com/2016/05/10/burning-woman/',
        # 'https://rockstarlavender.wordpress.com/2016/03/26/hello-barocco/',
        # 'https://rockstarlavender.wordpress.com/2016/03/05/end-of-an-era/',
        # 'https://rockstarlavender.wordpress.com/2015/12/29/2015-review/',
        # 'https://rockstarlavender.wordpress.com/2015/09/25/away-in-the-canaries-adventure-of-fashion-and/',
        # 'https://rockstarlavender.wordpress.com/2015/08/01/life-over-the-rainbow/',
        # 'https://rockstarlavender.wordpress.com/2015/05/11/the-arrival-of-lilith/',
        # 'https://rockstarlavender.wordpress.com/2015/04/18/the-time-of-zwischen/',
        # 'https://rockstarlavender.wordpress.com/2015/03/25/the-growing-of-a-spring-force/',
        # 'https://rockstarlavender.wordpress.com/2015/02/05/singing-a-rainbow/',
        # 'https://rockstarlavender.wordpress.com/2014/12/30/review-of-2014-the-wild-year-of-the-zebra/',
        # 'https://rockstarlavender.wordpress.com/2014/12/17/a-working-holiday-for-the-soul-at-chateau-challain/',
        # 'https://rockstarlavender.wordpress.com/2014/12/11/happy-birthday-to-my-son-evan-and-a-request-to/',
        # 'https://rockstarlavender.wordpress.com/2014/12/02/the-rainbow-is-a-she/',
        # 'https://rockstarlavender.wordpress.com/2014/11/06/the-rainbow-on-the-horizon/',
        # 'https://rockstarlavender.wordpress.com/2014/10/23/the-first-strokes-of-a-rainbow/',
        # 'https://rockstarlavender.wordpress.com/2014/09/10/pull-yourself-together/',
        # 'https://rockstarlavender.wordpress.com/2014/09/02/finding-solace-and-joy-in-surreal-fashion/',
        # 'https://rockstarlavender.wordpress.com/2014/08/29/seafaring-surreal-fashion-on-show/',
        # 'https://rockstarlavender.wordpress.com/2014/07/18/seven-months-seven-stars-made-bright-by-the/',
        # 'https://rockstarlavender.wordpress.com/2014/06/26/a-dream-and-an-awakening-shooting-the-surreal-for/',
        # 'https://rockstarlavender.wordpress.com/2014/06/25/what-are-you-worth/',
        # 'https://rockstarlavender.wordpress.com/2014/06/14/dont-wait-till-you-die-to-meet-your-soul/',
        # 'https://rockstarlavender.wordpress.com/2014/05/25/clear-skies-calm-seas-and-icelandic-adventures/',
        # 'https://rockstarlavender.wordpress.com/2014/04/28/if-you-hear-hoofbeats-in-kentucky/',
        # 'https://rockstarlavender.wordpress.com/2014/04/05/outpouring-live-to-the-world/',
        # 'https://rockstarlavender.wordpress.com/2014/02/21/what-little-evan-a-whizzing-yellow-stunt-plane/',
        # 'https://rockstarlavender.wordpress.com/2014/02/11/we-are-enough-because-we-are-love/',
        # 'https://rockstarlavender.wordpress.com/2014/01/20/my-letter-to-evan-and-to-the-world/',
        # 'https://rockstarlavender.wordpress.com/2013/12/31/review-2013/',
        # 'https://rockstarlavender.wordpress.com/2013/11/29/the-art-of-mother-and-child/',

        # 'http://www.jeffascough.com/sarah-portfolio-2015/',
        # 'http://www.topit.me/album/1224686',
        # 'http://www.alienskin.com/blog/2014/jeff-ascough/',
        # 'http://slide.tech.sina.com.cn/digi/slide_5_30939_46935.html',
        # 'http://www.kaixin001.com/repaste/75808361_2510883757.html',
        # 'http://thinkbyeye.blog.163.com/blog/static/1754203372010102711553673/',
        # 'http://www.imior.com/posts/5280'

        # 'http://digitalphotographycourses.co.za/jeff-ascough-remarkable-wedding-photographer/',
        # 'http://www.bhphotovideo.com/explora/photography/tips-and-solutions/im-not-wedding-photographer-conversation-jeff-ascough',
        # 'http://wanimal1983.org/',
        'http://item.jd.com/3141248.html',
    ]

    def parse(self, response):
        
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
           f.write(response.body) # 网页内容
        
        # image_path = '/Volumes/Liukelin/photos/fashionshootexperience.wordpress.com'

        # st = scrapy.selector(response=response).xpath('//img[@class="alignnone"]').extract()
        st = response.selector.xpath('//img/@src').extract() # 获取所有 img标签的 src属性  .re(r'[^/]*.[jpg|png|gif]$')
        # print "==%s==" % st
        # for img in st:
        #     image_path_name = "%s/%s" % (image_path, img.split("/")[-2])

        detailPicUrl = 'http://d.3.cn/desc/3141248?cdn=2&callback=showdesc'
        r = scrapy.Request(detailPicUrl)
        print "==%s==" %r.body

        
        item = DemoItem() #实例化我们自己定义item，可以理解为实例化字典
        item['image_urls'] = st    # url
        item['images'] = response.selector.xpath('//img/@src').re(r'[^/]*.[jpg|png|gif]$') # 保存图片   
        return item   









