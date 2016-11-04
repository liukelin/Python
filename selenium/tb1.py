#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains
import time
 
def login_tb():
        # Create a new instance of the Firefox driver
        #browser = webdriver.Firefox(executable_path = '/home/qianlu/software/geckodriver')
        browser = webdriver.Chrome(executable_path = '/home/qianlu/software/geckodriver') # 指定浏览器驱动
         
        # open baidu.com
        browser.get("https://login.taobao.com/member/login.jhtml?style=mini&from=alimama")
         
        # sleep 2 secs
        time.sleep(2)
         
        #clean the enter text
        browser.find_element_by_id("TPL_username_1").clear()
         
        #enter something
        browser.find_element_by_id("TPL_username_1").send_keys(u"")
        browser.find_element_by_id("TPL_password_1").send_keys(u"")
        time.sleep(1)
         
        #submit
        browser.find_element_by_id("J_SubmitStatic").click()
        #now_handle = browser.current_window_handle #获取当前窗口句柄
        #all_handles = browser.window_handles
        #for handle in all_handles:
        #    if handle != now_handle:
        #        print handle
        #        browser.switch_to_window(handle)

         
        # sleep 2 secs
        time.sleep(2)

        #source=browser.find_element_by_xpath("//*[@id='nc_1_n1z']")  
        #if not source:
        #    source=browser.find_element_by_xpath("//*[@id='nc_1_n1t']")  
        #if source:
        #    print 'yyy'
        #ActionChains(browser).drag_and_drop_by_offset(source,400,0).perform()
         
        time.sleep(60)
        browser.close()
if __name__ == "__main__":
    login_tb()
