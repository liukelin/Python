#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 网页截屏
# 
# # @author: liukelin  
import os
import sys
from selenium import webdriver
import time
 
def web_capture(url, save="capture.png"):
    # browser = webdriver.Firefox()
    # 使用内核打开浏览器
    browser = webdriver.Chrome(executable_path = 'driver/chrome/chromedriver-mac32')


    browser.set_window_size(1200, 900)
    browser.get(url) # Load page

    browser.implicitly_wait(2)

    time.sleep(1)

    browser.save_screenshot(save)
    browser.close()
 
 
if __name__ == "__main__":
    web_capture("http://www.redis.net.cn/tutorial/3511.html", 'capture1.png')