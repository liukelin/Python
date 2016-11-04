#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains
import time
 
def open_url():

	# browser = webdriver.Chrome(executable_path = 'driver/mozilla/mac-geckodriver')

	browser = webdriver.Firefox(executable_path = 'driver/mozilla/mac-geckodriver')

	
	browser.get("https://baidu.com")

	browser.find_element_by_id("kw").send_keys(u"网易邮箱")

	time.sleep(1)

	browser.find_element_by_id("su").click()

	time.sleep(2)

	browser.find_element_by_id("op_email3_username").send_keys(u"liukelin_1@163.com")

	browser.find_element_by_class("op_email3_password").send_keys(u"qq62807346280734")

	browser.find_element_by_class("op_email3_submit").click()

	time.sleep(2)

if __name__=='__main__':
	open_url()