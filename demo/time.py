#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 对于时间的操作，记录
#

import datetime
import time 

today1 = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
print "当前时间:%s" %today1

d1 = datetime.datetime(2016, 01, 01)
d2 = datetime.datetime(2016, 03, 01)
print "日期间隔天数:%s" % (d2 - d1).days

today = datetime.date.today()
day = today - datetime.timedelta(days=1)
day1 = today - datetime.timedelta(days=-1)
print "前一天:%s,后一天:%s" % (day,day1)

a = "2016-04-10 23:40:00"
timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
timeStamp = int(time.mktime(timeArray))
print "字符串时间转换为时间格式:%s" % timeStamp

d2 = "2016-04-10 23:40:00"
d2 = datetime.datetime.strptime(d2 , "%Y-%m-%d %H:%M:%S")
print "字符串时间转换为时间格式:%s" % timeStamp


s = datetime.datetime.utcfromtimestamp(2233333333)
print "字符串时间戳转换时间格式:%s" % s


print str(time.time()).split(".")[0]