#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016
# @author: liukelin
#
'''
test
'''
import json
import re
import time

a = '130****0009@163.com'
b = '0130***@163.com'

a1 = a.split('@')
b1 = b.split('@')

# print a1[0][-4:],b1[0][:-3]

ass = {}
ass = {
	'asa':1,
}
# if len(ass)==0:
# 	print 111

# print 6875974916%12


a = {'msg':'马克吐温'}
print a
print a['msg']
print json.dumps(a)
print json.dumps(a, ensure_ascii=False)

s = 0.009999
s1 = float(int(s*100))/100
print s1
if s1<=0:
    print 2


ss = [
    {'a':1},
    {'a':2},
]
st = [s['a'] for s in ss]
print st



# global cookie
def set_cookie():
    global cookie
    cookie = 'make'


set_cookie()
print cookie


k = 0
for i in range(0,10):
    k += 1
print k


# python不能在遍历里面删除 list自身元素
ulist = [{'a':1}, {'b':2}, {'c':3}, {'d':4} ]
print type(ulist)
print type(ulist[:])

for i in ulist[:]: # 复制list成为新的list
    ulist.remove(i)
print ulist

ulist = [{'a':1}, {'b':2}, {'c':3}, {'d':4} ]
# for i in range(0, len(ulist)):
#     ulist.remove(ulist[i])
# print ulist

a = ''
if a:
    print 'a'
ss = {'a':1}
c = ss['b'] if ss.get('b') else 0
print c
print ss.get('b')

a = 10000017
print str(a)[-2:]

a = "170120120"
print "20"+a[:-3]
ass = [1,2,3]
st = [str(i) for i in ass]
print st



print (11779512556 + 0)%24 +10000001
print (11779512556 + 03145)%24 +10000001

# 10000076
print "===="
a = 03145
a = "%s" %a
print a
a = str(a)
print a
print int(a,10)
print int(a)
# print int(a)
# print re.sub(r"\b0*([1-9][0-9]*|0)", r"\1", a)  
# 

skk = [1 ,1,2, 3,4,6,5]
print min(skk)

import os
print os.path.dirname(os.path.abspath(__file__))


oneTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime( time.time() ))
if str(oneTime) > '2017-01-26 00:00:00':
    print str(oneTime)
    
i = 'aaaa====23123'
st = i.split('====')
print st








