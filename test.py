#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: liukelin  314566990@qq.com
import time
import datetime
import urllib3
import string
import re
import sys

# reload(sys)
# sys.setdefaultencoding('utf8')

# print("==%s==" % time.time())
# print("==%s==" % time.time())

def get_html(url):
	http = urllib3.PoolManager()
	r = http.request('GET', url)
	m = r.data
	
	page_data = m.decode('UTF-8')
	page_ = re.compile('<img src=\"(.+?)\"')#匹配img正则

	for d in page_.findall(page_data):
		pass

def up_num():
	# 问题：有两个数，之和是两位数，且这两个数字相同；之积是三位数，且这三个数字相同，求这两个数。
	for i in range(1,100):
		for k in range(1,100):
			st1 = i+k
			st2 = i*k

			if len(str(st1))!=2:
				continue
			if len(str(st2))!=3:
				continue
			if st1/int(str(st1)[0])!=11:
				continue
			if st2/int(str(st2)[0])!=111:
				continue

			print(i,k)
up_num()

image = 'http://d.3.cn/desc/1856588?cdn=2&callback=showdesc'
http = urllib3.PoolManager()
m2 = http.request('GET', image)
image_data = m2.data
print(image_data)









	check_ = db.mysql.get("SELECT * FROM `global_orders` where `uid`=%s  AND `note` LIKE  '%%%s%%'  ", uid, note)
































