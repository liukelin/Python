#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016
#
# @author: liukelin

# 抓取京东商品详情页面

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print "BASE_DIR=", BASE_DIR
# sys.path.append("/home/wu/Aptana Studio 3 Workspace/suoping")
sys.path.append(BASE_DIR)
import urllib3
import string
import re
import json
import tornado.web
#import constants
#import ujson as json
import time
import yaml
import torndb
import db
# import redis
import random
# import utils
from datetime import date, datetime, timedelta
import os
# from models import goods

reload (sys)
sys.setdefaultencoding('utf-8')

SETTINGS_FILE = BASE_DIR + "/settings.yaml"

# MySQL数据库连接配置
try:
    config = yaml.load(file(SETTINGS_FILE, 'r')) 
except yaml.YAMLError as e:
    print "Error in configuration file: %s" % e

# 数据库连接实例
myConn = torndb.Connection(**config['mysql'])

#保存路径
dir_file = "%s/static" % sys.path[0]

# 图片域名指向路径
image_small_file = "/image/small/"
image_detail_file = "/image/detail/"
html_detail_file = "/html/"

template_html = "%s/gethtml/template.html" % sys.path[0]

def get_jd(url):
    data = {}
    ts = url.split("/")
    productid = str(ts[len(ts)-1].split(".")[0])

    print "=start:%s=" %url

    http = urllib3.PoolManager()
    # title 
    m0 = http.request('GET', url, timeout=10)
    page = m0.data

    print "=page:ok="

    '''
    '''
    data['goods_url'] = url
    data['goods_code'] = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))+ str(random.randint(10,99))

    # 商品详细信息
    '''
    idx = page.find('product:')
    print "=%s=" %idx
    if idx>=0:
        idx += 8
        res = re.search(r'{.+?}', page[idx:])
        # text = json.loads(res.group())
        print "=%s=" % res.group()
    '''
    product_re = re.compile(r'product: (.*?);' , re.S)
    product_info = re.findall(product_re, page)[0]
    # data_json = product_info.decode('gbk') 
    name_re = re.compile(r"name: '(.*?)',")
    name = re.findall(name_re, product_info)[0]
    data['goods_name'] = name.decode('unicode-escape')
    # print "=%s=" % data['name']
    print "=goods_name:ok=" 

    #获取轮播图
    flash_re = re.compile(r'<div id="spec-list"(.*?)</div>', re.S)
    flash_info = re.findall(flash_re, page)[0]
    name_re = re.compile(r"src='(.*?)'")
    flashUrl = re.findall(name_re, flash_info)

    arr = []
    for i in flashUrl:
        img_url = "http:%s" % i
        # iphone 
        img_url = img_url.replace('s54x54','s450x450') # s300x300

        #mac
        img_url = img_url.replace('n5/','n1/') # n5

        check_dow = down_img(img_url , dir_file+image_small_file, http)
        if check_dow:
            arr.append(image_small_file+check_dow)
    data['goods_image'] = arr
    # print "=%s=" % data['flashUrl']
    print "=goods_image:ok=" 

    # 获取商品价格
    priceUrl = 'http://p.3.cn/prices/get?skuid=J_' + productid
    m1 = http.request('GET', priceUrl, timeout=10)
    try:
        data['goods_price'] = json.loads(m1.data)[0]['p']
    except:
        data['goods_price'] = 0
    # print "==%s==" % ( data['goods_price'])
    print "=price:ok=" 

    # 获取详细信息大图
    detailPicUrl = 'http://d.3.cn/desc/'+ productid + '?cdn=2&callback=showdesc'
    m2 = http.request('GET', detailPicUrl, timeout=10)
    detail = m2.data.replace('\\','')
    detail_re = re.compile(r'data-lazyload="(.*?)"')
    ImageUrl = re.findall(detail_re, detail)
    arr = []
    for i in ImageUrl:
        img_url = "http:%s" % i
        check_dow = down_img(img_url , dir_file+image_detail_file, http)
        if check_dow:
            arr.append(image_detail_file+check_dow)
    data['goods_detail'] = arr

    print "=ImageUrl:ok=" 

    goods_html = set_template_html(dir_file+html_detail_file, arr, data['goods_code'], data['goods_name'])
    if goods_html:
        data['goods_html'] = html_detail_file + goods_html
    else:
        data['goods_html'] = ''
    print "=goods_html:ok=" 

    # print data
    set_goods(data)
    return data

def down_img(url, file_, http2):
    try:
        img = http2.request('GET', url, timeout=15)
        image_data = img.data
    except:
        http2 = urllib3.PoolManager()
        img = http2.request('GET', url, timeout=15)
        image_data = img.data

    fneme = url.split('.')[-1]
    if fneme.lower() not in ['jpg','png','gif','bmp','jpeg']:
        return False
    img_name = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))+ str(random.randint(100,999)) +'.'+ fneme
    file_name = file_+img_name
    today = str(date.today())
    try:
        # 保存图片到文件夹
        with open(file_name, 'wb') as up:
            up.write(image_data)

    except:
        print "=dowimg error:%s=" %url
        return False


    return today+ '/' +img_name

'''
    生成详情页面
'''
def set_template_html(file_, ImageUrls, goods_code, goods_name):
    fileName = str(goods_code) +'.html'


    html = ''
    try:
        fileObj = open(template_html, 'r')
        html = fileObj.read()
    except:
        try:
            if fileObj:
                fileObj.close()
        except:
            pass

    img_html = ' '
    for i in ImageUrls:
        # print i
        img_html = img_html + '<img src="' + 'http://static.duobao.com.s3-website.cn-north-1.amazonaws.com.cn' + i + '" style="width:100%;margin:0 auto; height:auto;"/>'
    html = html.replace("{{detail}}", img_html).replace("{{title}}", goods_name)
    # print html


    today = str(date.today())
    file_path = file_ + today + '/'
    file = file_path + fileName
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    try:
        with open(file, 'wb') as up:
            up.write(html)
    except Exception,e:
        print "=dowHTML error"
        print e
        return False

    return today+ '/' +fileName


def set_goods(data):
    goods_image =  json.dumps(data['goods_image'])
    goods_detail = json.dumps(data['goods_detail'])
    goods_code = data['goods_code']
    data  = {
            'goods_code' :data['goods_code'],
            'goods_title' :data['goods_name'],
            'goods_name' :data['goods_name'],
            'goods_image' :goods_image,
            'goods_detail' :goods_detail,
            'goods_price' :data['goods_price'],
            'goods_market_price' :data['goods_price'],
            'goods_cost_price' :data['goods_price'],
            'goods_html':data['goods_html'],
            'goods_url':data['goods_url']
        }
    # print goods_detail
    # new_id = goods.set_goods(data)
    createtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    data['goods_update_time'] = data['goods_update_time'] if data.has_key('goods_update_time') else createtime
    data['goods_create_time'] = data['goods_create_time'] if data.has_key('goods_create_time') else createtime
    new_id = myConn.execute("INSERT INTO  `product` ("
            "`goods_code`, `goods_title` ,`goods_name` ,`goods_image` ,`goods_detail` ,`goods_price` ,"
            "`goods_market_price` , `goods_cost_price` ,`goods_update_time` ,`goods_create_time`,`goods_html`,`goods_url`)"
            "VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                data['goods_code'] ,
                data['goods_title'] ,
                data['goods_name'] ,
                data['goods_image'] ,
                data['goods_detail'] ,
                data['goods_price'] ,
                data['goods_market_price'] ,
                data['goods_cost_price'] ,
                data['goods_update_time'] ,
                data['goods_create_time'],
                data['goods_html'],
                data['goods_url'],
            )

    print "=add goods:%s=" % new_id
    return new_id


if __name__ == "__main__":
    urls = [
    #         # 'http://item.jd.com/2385655.html',
    #         # 'http://item.jd.com/2515831.html',
    #         # 'http://item.jd.com/1514838.html',
    #         # 'http://item.jd.com/2473905.html',
    #         # 'http://item.jd.com/2740923.html',
    #         # 'http://item.jd.com/1593516.html',
    #         # 'http://item.jd.com/1593512.html',
    #         # 'http://item.jd.com/2742853.html',
    #         # 'http://item.jd.com/2644896.html',
    #         # 'http://item.jd.com/2570797.html',
    #         # 'http://item.jd.com/3028389.html',
    #         # 'http://item.jd.com/3133498.html',
    #         # 'http://item.jd.com/3031737.html',
    #         # 'http://item.jd.com/2908675.html',
    #         # 'http://item.jd.com/2805806.html',
    #         # 'http://item.jd.com/1688565.html',
    #         # 'http://item.jd.com/2529539.html',
    #         # 'http://item.jd.com/2714736.html',
    #         # 'http://item.jd.com/2180641.html',
    #         # 'http://item.jd.com/1689980.html',
    #         # 'http://item.jd.com/2143016.html',
    #         # 'http://item.jd.com/2060604.html',
    #         # 'http://item.jd.com/1584011175.html'
    #
            'http://item.jd.com/2442033.html'
        ]

    get_jd(url)

