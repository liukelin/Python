#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: liukelin  314566990@qq.com
# 多线程 抓取 https 图片
# 
dir_ = os.getcwd()

def set_logs(msg,file=''):
    logStr = "[%s]%s\r\n" %(time.strftime("%Y-%m-%d %H:%M:%S"),msg)
    file = file if file!='' else dir_
    f = open('%s/logs.log' % file,'a')
    f.write(logStr)
    f.close()

