#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2016
# @author: liukelin
#
'''
test 邮箱入库
'''

import os
import sys
import time
# import yaml
import torndb
import db
import redis
import random
# import utils
# import urllib3
import json 
from datetime import date, datetime, timedelta
# import pymysql



# config = {
# 	'mysql':{
# 		'host': '192.168.1.86',
# 		'port':3306,
# 	    'db': 'netease_mail', 
# 	    'user': 'canal',
# 	    'password': 'canal', 
# 	}
# }
config = {
	'mysql':{
		'host': '127.0.0.1',
	    'database': 'netease_mail', 
	    'user': 'root',
	    'password': '123456', 
	}
}


# conn = pymysql.connect(**config['mysql'])
# cur = conn.cursor()
# cur.execute("SELECT * FROM user")
# for r in cur.fetchall():
#            print(r)
#            #cur.close()
# conn.close()

# 数据库连接实例
db.mysql = torndb.Connection(**config['mysql'])


def get_txt(dir_):
	num = 100 # 5000入库一次
	i = 0
	data = []
	f = open(dir_, "r")  
	while True:  
	    line = f.readline()  
	    if line:
	        line=line.strip()
	        if line:
	        	type_ = ''
	        	d = line.split('@')
	        	if isinstance(d , (list)) and len(d)>1:
	        		type_ = d[1]

	        	data.append([line, type_ ])
	        	if i>0 and i%num==0:
	        		set_data(data)
	        		data = []
	        	i=i+1
	    else:  
	        break
	f.close()


# 批量入库
def set_data(body=[]):
	'''
	d = []
	for i in body:
		if i[0] and i[1]:
			msg = "('%s','%s')" %(i[0],i[1])
			d.append(msg)
	data = ','.join(d)
	sql = " insert into `duobao_user` (`mail`,`type_`) values %s " % data
	# print(sql)
	# exit
	# 
	'''
	# conn = pymysql.connect(**config['mysql'])
	# cur = conn.cursor()
	for i in body:
		if i[0] and i[1]:
			sql = " insert into `duobao_user` (`mail`,`type_`) values ('%s','%s') " % (i[0],i[1])
			db.mysql.execute(sql)
	# conn.close()

	return len(body)

if __name__=='__main__':
	get_txt('/Users/liukelin/Downloads/record_user_com.txt')





