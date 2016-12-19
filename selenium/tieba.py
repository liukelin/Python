#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# # @author: liukelin  314566990@qq.com
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
def baidutieba(users):

	# 使用模拟GUI
	# display = Display(visible=0, size=(1024, 768))
	# display.start()

	# 使用内核打开浏览器
	browser = webdriver.Chrome(executable_path = 'driver/chrome/chromedriver-mac32')

	# 手机网页可以不用验证码
	url = 'https://wappass.baidu.com/passport/?login&tpl=wimn&subpro=wimn&regtype=1&u=https%3A%2F%2Fm.baidu.com/usrprofile%23logined'
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

	# 获取网页cookie
	cookie = [item["name"] + "=" + item["value"] for item in browser.get_cookies()]
	cookiestr = ';'.join(item for item in cookie)

	time.sleep(3)
	print(cookiestr)

	# 关注贴吧
	# like_tieba(i, browser)

	browser.quit() # 关闭浏览器
	# display.stop() # 关闭GUI
	

	# search = get_my_like(cookiestr) # 获取关注列表
	search = ['国际米兰', '完美世界小说', '李毅', '遮天', '坦克世界', '显卡', '广州', '基友你永远不会独行', '熟女', '恐怖', '魔兽世界', '美食', '隐居', '广东', '灵异', '电影', '美女', '配置', '美国', '鬼', '平行宇宙', '手工', 'lol', '后宫动漫', '陆龟', '新里番', '狗', '里漫', '海拉尔', '灵魂', '女头', '情侣动漫', '动漫', '里番动画', '内涵', '胥渡', '里番', '模型', '深海恐惧症', 'yiciy', '帝吧', '周杰伦', '腐女', '坚持', '我欲封天', '戒撸', '电脑', '情人', '客家', '高达', '蕾丝', '天河', '周杰伦中文网', '中国好声音', '手机', '稀翔', '妹子', '剑灵', '情感', '啦啦啦小帝', '非主流', '人与动物', '减肥', '网络游戏', '34d', '龟', '游戏策划', '黑丝', '新姐脱', '珠海', '游戏开发', '英雄联盟', '激战2', '手办', '盗墓笔记', '舌尖上的中国', '仙剑奇侠传', 'macbook', '赣州', '美少妇', '调戏小妞', 'unity3d', '2012', '巴塞罗那', '乌龟', 'macbookpro', '切尔西', '广州大学', '大众高尔夫', '沉珂', '汽车', '国米女生', '汽车之家', '苹果', '皇家马德里', '马甲线', '新百伦', 'ac米兰', 'iphone', '珠海二中', 'polo', '金庸', '观赏鱼', '戒色', '手机游戏', '于都三中', '丰胸', 'wolferl', '南方it学院', '单反', '绫濑遥', '于都中学', '圣墟', '传统弓箭', '鱼', 'mini', '北京师范大学珠海分校', '广东南方职业学院', '健身', '装修', '国米修车', '广东南方学院', '小杰是个好姑娘', '女神', '摄影', '现代弓箭', '寒武纪年', '风水', '热带鱼', '女子戒色', '中山大学', '中山大学珠海校区', '备胎', '未解之谜', '恐怖片', '游戏', '珠海南方it学院', '情侣', '感情', '蓝颜', 'sd敢达', '我的机器人女友', '曼联', '腐漫', '2ch', '虚幻4', '阅经', '战机世界', '小吃', '婺源', '渡边麻友', 'lofter', '北京理工大学珠海学院', '扒皮', '强身健体', '节欲养生', '独木舟', '广州天河', '女sm', '健美裤', 'deepweb']
	yess = sign_tieba(cookiestr, search) # 使用curl库 请求签到
	
	print(users[0]+',ok.')

	return yess
	
def login2():
	tt = int(time.time()) * 1000
	loginUrl = 'https://wappass.baidu.com/wp/api/login?tt=%s' %str(tt)

# 关注
def like_tieba(ba, browser=None):
	tiebas = ['国际米兰', '完美世界小说', '李毅', '遮天', '坦克世界', '显卡', '广州', '基友你永远不会独行', '熟女', '恐怖', '魔兽世界', '美食', '隐居', '广东', '灵异', '电影', '美女', '配置', '美国', '鬼', '平行宇宙', '手工', 'lol', '后宫动漫', '陆龟', '新里番', '狗', '里漫', '海拉尔', '灵魂', '女头', '情侣动漫', '动漫', '里番动画', '内涵', '胥渡', '里番', '模型', '深海恐惧症', 'yiciy', '帝吧', '周杰伦', '腐女', '坚持', '我欲封天', '戒撸', '电脑', '情人', '客家', '高达', '蕾丝', '天河', '周杰伦中文网', '中国好声音', '手机', '稀翔', '妹子', '剑灵', '情感', '啦啦啦小帝', '非主流', '人与动物', '减肥', '网络游戏', '34d', '龟', '游戏策划', '黑丝', '新姐脱', '珠海', '游戏开发', '英雄联盟', '激战2', '手办', '盗墓笔记', '舌尖上的中国', '仙剑奇侠传', 'macbook', '赣州', '美少妇', '调戏小妞', 'unity3d', '2012', '巴塞罗那', '乌龟', 'macbookpro', '切尔西', '广州大学', '大众高尔夫', '沉珂', '汽车', '国米女生', '汽车之家', '苹果', '皇家马德里', '马甲线', '新百伦', 'ac米兰', 'iphone', '珠海二中', 'polo', '金庸', '观赏鱼', '戒色', '手机游戏', '于都三中', '丰胸', 'wolferl', '南方it学院', '单反', '绫濑遥', '于都中学', '圣墟', '传统弓箭', '鱼', 'mini', '北京师范大学珠海分校', '广东南方职业学院', '健身', '装修', '国米修车', '广东南方学院', '小杰是个好姑娘', '女神', '摄影', '现代弓箭', '寒武纪年', '风水', '热带鱼', '女子戒色', '中山大学', '中山大学珠海校区', '备胎', '未解之谜', '恐怖片', '游戏', '珠海南方it学院', '情侣', '感情', '蓝颜', 'sd敢达', '我的机器人女友', '曼联', '腐漫', '2ch', '虚幻4', '阅经', '战机世界', '小吃', '婺源', '渡边麻友', 'lofter', '北京理工大学珠海学院', '扒皮', '强身健体', '节欲养生', '独木舟', '广州天河', '女sm', '健美裤', 'deepweb']
	try:
		# url = 'http://tieba.baidu.com/f?ie=utf-8&fr=search&kw=%s' %ba[0]
		# browser.get(url)
		# browser.find_element_by_id("j_head_focus_btn").click()
		'''
		https://tieba.baidu.com/mo/q/favolike?uid=357041565&itb_tbs=268f336388a116841479976272&fid=661506&kw=黄轩吧
		http://tieba.baidu.com/f/like/commit/add 
		名称	值
		fid	238326
		fname	黄轩
		uid	%E7%81%8C%E9%98%B4%E4%BC%BC%E7%AE%AD&ie=utf-8
		ie	gbk
		tbs	907d0e4e91d078ec1479977007
		'''
		url = 'https://tieba.baidu.com/mo/q/favolike'
	except:
		pass

# 发帖
def add_tie(ba, title, msg, browser=None):
	url = 'http://tieba.baidu.com/f?ie=utf-8&fr=search&kw=%s' %ba
	title 

'''
	# 获取关注列表
'''
def get_my_like(Cookie):
	# 获取关注列表header
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
	return search


'''
	# 签到
	search 关注的吧列表
'''
def sign_tieba(Cookie, search=[]):
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
	return search


if __name__=='__main__':
	# 百度账号+密码
	tiebaUser = [
		# ['账号1', 'xxx'],
		# ['账号2', 'xxx'],
	]
	for i in tiebaUser:
		baidutieba(i)
		




