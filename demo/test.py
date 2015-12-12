#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

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






