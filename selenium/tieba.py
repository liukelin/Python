#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
# from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
# from selenium.webdriver.common.action_chains import ActionChains
# from pyvirtualdisplay import Display # 模拟GUI窗口 依赖于Xvfb
import time
import requests
import re
import json

# login
def baidutieba(users=[]):

	# 使用模拟GUI
	# display = Display(visible=0, size=(1024, 768))
	# display.start()

	# 使用内核打开浏览器
	browser = webdriver.Chrome(executable_path = 'driver/chrome/chromedriver-mac32')

	# 手机网页可以不用验证码
	url = 'https://wappass.baidu.com/passport/?login&tpl=wimn&ssid%3D0%26amp%3Bfrom%3D844b%26amp%3Buid%3D%26amp%3Bpu%3Dsz%25401320_2001%252Cta%2540iphone_1_10.0_3_602%26amp%3Bbd_page_type%3D1&tn=&regtype=1&u=https%3A%2F%2Fm.baidu.com'
	browser.get(url)
	# 输入账号密码
	browser.find_element_by_name("username").send_keys(users[0])
	browser.find_element_by_name("password").send_keys(users[1])
	time.sleep(1)
	# 点击登录
	browser.find_element_by_id("login-submit").click()

	time.sleep(2)

	try:
		browser.find_element_by_partial_link_text("跳过").click()
	except:
		pass

	# 关注贴吧
	# like_tieba('稀翔', browser)

	# 获取网页cookie
	cookie = [item["name"] + "=" + item["value"] for item in browser.get_cookies()]
	cookiestr = ';'.join(item for item in cookie)

	browser.quit() # 关闭浏览器
	# display.stop() # 关闭GUI
	
	baidutieba2(cookiestr) # 使用curl库 请求签到
	
	print(users[0]+',ok.')
	
def login2():
	tt = int(time.time()) * 1000
	loginUrl = 'https://wappass.baidu.com/wp/api/login?tt=%s' %str(tt)

# 关注
def like_tieba(ba, browser=None):
	url = 'http://tieba.baidu.com/f?ie=utf-8&fr=search&kw=%s' %ba
	browser.get(url)
	browser.find_element_by_id("j_head_focus_btn").click()

# 发帖
def add_tie(ba, title, msg, browser=None):
	url = 'http://tieba.baidu.com/f?ie=utf-8&fr=search&kw=%s' %ba
	title 

# 签到
def baidutieba2(Cookie):
	# Please replace you cookie here.
	Cookie = Cookie

	# 签到header
	headers = {
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
		'Connection': 'keep-alive',
		'Content-Length': '61',
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'Cookie': Cookie,
		'DNT': '1',
		'Host': 'tieba.baidu.com',
		'Origin': 'http://tieba.baidu.com',
		# 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
		# 'User-Agent': 'iOS / Safari 7: Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53',
		# 'User-Agent': 'iOS / Chrome 34: Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) CriOS/34.0.1847.18 Mobile/11B554a Safari/9537.53',
		'User-Agent': 'Android / Chrome 34: Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36',
		'X-Requested-With': 'XMLHttpRequest',
		}
	# 列表header
	headers1 = {
		"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"Accept-Encoding":"gzip, deflate, sdch",
		"Accept-Language":"zh-CN,zh;q=0.8",
		"Cache-Control":"max-age=0",
		"Connection":"keep-alive",
		"Cookie": Cookie,
		"Host":"tieba.baidu.com",
		"Upgrade-Insecure-Requests":"1",
		# "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36"
		# "User-Agent":"iOS / Safari 7: Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53"
		#'User-Agent': 'iOS / Chrome 34: Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) CriOS/34.0.1847.18 Mobile/11B554a Safari/9537.53',
		'User-Agent': 'Android / Chrome 34: Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36',
		}

	url_forum = 'http://tieba.baidu.com/f/like/mylike' 
	r2 = requests.get(url_forum, headers=headers1)

	# 获取总页数
	try:
		pages = re.findall(r'a href=(.*?)">尾页',r2.text)
		page = int(pages[0].split('=')[1])
	except:
		page = 1

	search = []
	for i in range(1, page+1):
		if i>1:
			url_forum = 'http://tieba.baidu.com/f/like/mylike?&pn=%s' %str(i)
			r2 = requests.get(url_forum, headers=headers1)

		# 获取贴吧标题
		tiebaNames = re.findall(r'a href=.*?title="(.+?)">',r2.text)
		if len(tiebaNames)>0:
			search.extend(tiebaNames)

	print('num:%s' %len(search))
	print(search)

	# 签到
	for i in search:
		try:
			payload = {'ie': 'utf-8', 'kw': i, 'tbs': 'fb6ecec1996df5c41435580832'}
			r = requests.post('http://tieba.baidu.com/sign/add', data=payload, headers=headers, timeout=3)
			print(json.loads(r.text))
		except:
			pass
		print(i+",success")
		'''
		html = r.text.decode('raw_unicode_escape')
		if html == u'{"no":1101,"error":"亲，你之前已经签过了","data":""}':
		'''
	print('over')


if __name__=='__main__':
	# 百度账号+密码
	tiebaUser = [
		['账号1', 'xxx'],
		['账号2', 'xxx'],
		
	]
	for i in tiebaUser:
		baidutieba(i)



