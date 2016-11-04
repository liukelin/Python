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


'''
	对生成的顺序数字 ， 分配比例
'''
def rangeForRank(total):
	users = []
	list_ = [0.6, 0.32, 0.07, 0.01]

	dobleList = {0:0}
	for i in range(0, len(list_)):
		if i < 1:
			dobleList[i+1] = round(total * list_[i])
		else:
			dobleList[i+1] = round(total * list_[i] + dobleList[i])

	print dobleList

	for i in range(0, total+1):
		for j in range(1, len(dobleList)):
			if i > dobleList[j-1] and i <= dobleList[j]:
				users.append( { 'i':i, 'type': list_[j-1] } )
	return users

ss = rangeForRank(10)
print "==="
print len(ss),ss


a = [1,2,3,4,5,6,7,8,9]
b = [1,1,2,3]
codesNew = list( set(a).difference( set(b) ) )
print codesNew

















