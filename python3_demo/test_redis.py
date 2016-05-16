#!/usr/bin/python3
# -*- coding:utf8 -*-

import redis


r = redis.Redis(host='localhost', port=6379, db=0)

for i in range(0 , 100):
	r.zadd('myset2',i,i)
	print(i)