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
