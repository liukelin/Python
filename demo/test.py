#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import os
import datetime

print "hello python"


def test(n) :
    k=1
    for i in range(1,n+1):
        k = k*i
    return k
print test(5)


s = []
ks = None
s.append(ks)

print s

json_str = '["s",{"asd":"asdsss"}]'
arr = json.loads(json_str)
for i in arr:
	if i <> 's':
		print i["asd"]

x = 5
y = 6
x = [x,y]
y = x[0]
x = x[1]
print "x:%s, y:%s" %(x,y)

#
# 打印时间段内的日期
#
start = datetime.datetime(2016,01,01)
end = datetime.datetime(2016,03,01)

# start = datetime.strptime("2007-03-04 21:08:12", "%Y-%m-%d %H:%M:%S")
# end = datetime.strptime("2007-04-04 21:08:12", "%Y-%m-%d %H:%M:%S")
for x in range(0, (end - start).days):
	day_ = datetime.timedelta(x)
	day = start + day_
	print day








