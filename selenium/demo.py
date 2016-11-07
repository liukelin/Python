#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains
import time
'''
	find_element_by_id
	find_element_by_name
	browser.find_element_by_id('kw1').get_attribute('type') # 获取元素值
	browser.find_element_by_xpath(".//*[@id='login']").send_keys(Keys.ENTER) # 按下enter
	article = browser.find_element_by_link_text(u'周碧华：社科院出现内鬼意味着什么？')
	ActionChains(browser).move_to_element(article).perform()#将鼠标移动到这里，但是这里不好用
	ActionChains(browser).context_click(article).perform()
	
	http://www.cnblogs.com/fnng/p/3183777.html
	· id
	· name
	· class name
	· link text
	· partial link text
	· tag name
	· xpath
	· css selector
	#通过id方式定位
	browser.find_element_by_id("kw").send_keys("selenium")

	#通过name方式定位
	browser.find_element_by_name("wd").send_keys("selenium")

	#通过tag name方式定位
	browser.find_element_by_tag_name("input").send_keys("selenium")

	#通过class name 方式定位
	browser.find_element_by_class_name("s_ipt").send_keys("selenium")

	# 通过link名定位（全名）
	browser.find_element_by_link_text("贴 吧").click()
	
	# Partial Link Text 定位 （模糊link名）
	browser.find_element_by_partial_link_text("贴").click()

	#通过CSS方式定位
	browser.find_element_by_css_selector("#kw").send_keys("selenium")

	#通过xphan方式定位
	browser.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")

	'''

def demo():
	
	# browser = webdriver.Chrome(executable_path = 'driver/mozilla/mac-geckodriver')

	browser = webdriver.Firefox(executable_path = 'driver/mozilla/mac-geckodriver')

	
	browser.get("https://baidu.com")

	browser.find_element_by_id("kw").send_keys(u"网易邮箱")

	time.sleep(1)

	browser.find_element_by_id("su").click()

	time.sleep(2)

	# 获取网页cookie
	cookie = [item["name"] + "=" + item["value"] for item in browser.get_cookies()]
	cookiestr = ';'.join(item for item in cookie)
	print("=cookie:%s=" % cookiestr)

	browser.find_element_by_id("op_email3_username").send_keys(u"liukelin_1@163.com")

	browser.find_element_by_class_name("op_email3_password").send_keys(u"qq6280734")

	browser.find_element_by_class_name("op_email3_submit").click()

	time.sleep(2)

	browser.quit() #关闭

def open_apple():
	
	browser = webdriver.Firefox(executable_path = 'driver/mozilla/mac-geckodriver')
	
	browser.get("https://appleid.apple.com/account#!&page=create")

	time.sleep(5)

	# 获取验证码图片
	# ss = browser.find_element_by_class_name("idms-captcha-wrapper")
	ss = browser.find_element_by_css_selector("img[width=\"120\"]").get_attribute('src')
	imgdata = ss.replace('data:image/jpeg;base64,', '')
	
	import base64   
	imgdata=base64.b64decode(imgdata)  
	file=open('%s.jpeg' %str(time.time()),'wb')  
	file.write(imgdata)  
	file.close() 
	

if __name__=='__main__':
	open_apple()










