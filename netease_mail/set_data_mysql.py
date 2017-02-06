#!/usr/bin/env python
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
# import db
import redis
import random
# import utils
# import urllib3
import json 
from datetime import date, datetime, timedelta
# import common

config = {
	'mysql':{
		'host': '127.0.0.1',
	    'database': 'netease_mail_all', 
	    'user': 'root',
	    'password': '123456', 
	},
	'redis':{
		'host': '127.0.0.1',
	    'port': 6379,
	    'db':0 
	}
}

dir_ = ''
path_s = [
			'126',
			'163com',
			'1632',
			'163mail1',
			'163mail2',
			'163mail3',
			'163mail4',
			'163mail5',
			'163mail6',
			'163mail7',
			'163mail8',
		]
num = int(sys.argv[1])
if path_s[num]:
	path_ = dir_ + path_s[num]
else:
	exit('error no file !')


st = os.popen('ps -ef | grep "'+__file__+' '+ str(num) +'" | grep -v "grep" | wc -l' ).read().strip('\n').strip()
if int(st)>2: # 允许进程数
    exit('process Max %s No.:%s' %(__file__, st))
    # exit()


# 数据库连接实例
myConn = torndb.Connection(**config['mysql'])

pool = redis.ConnectionPool(**config['redis'])
redisConn = redis.Redis(connection_pool=pool)

file_check = ["txt"]#文件限制

# 读取所有文件
def get_txt_list(path):
    try:
        print "开始：%s" %(path)
        for i in os.listdir(path):
            temp_dir = os.path.join(path,i)
            if os.path.isdir(temp_dir):
                get_txt_list(temp_dir);
            else:
                if i.split('.')[-1].lower() in file_check:
                    # dirs[thread].append(temp_dir)
                    # shutil.copyfile(temp_dir,os.path.join(file_src,thread,i))
                    
                    print "处理:%s" %(temp_dir)
                    #check out file
                    check = redisConn.get(temp_dir)
                    if not check:
                    	# 读取文件
	                    get_txt(temp_dir)

	                    redisConn.set(temp_dir, 1)
                                        
                    else:
                    	print "已处理。"
    except:
        print 'Have no legal power' 
    return True

def get_txt(temp_dir):
	try:
		isDIR = temp_dir.replace(dir_, '')
	except:
		pass

	num = 5000 # 5000入库一次
	i = 0
	data = []
	f = open(temp_dir, "r")
	while True:  
	    line = f.readline()  
	    if line:
	    	try:
		        line=line.strip()
		        if line:
		        	# 普通格式
		        	d = line.split('----')
		        	if isinstance(d , (list)) and len(d)>1:
		        		d.append(isDIR)
			        	data.append(d)
			        else:
			        	for t in ['.com','.cn']:
			        		dk = line.split(t)
			        		if isinstance(dk , (list)) and len(dk)>1:
			        			data.append([dk[0]+t, dk[1]],isDIR)
			        if i>0 and i%num==0:
			        	set_data(data)
			        	data = []
			        i=i+1
			except:
				pass
	    else:  
	        break
	f.close()



# 批量入库
def set_data(body=[]):
	'''
	d = []
	for i in body:
		if i[0] and i[1]:
			msg = "(%s,'%s')" %(i[0],i[1])
			d.append(msg)
	data = ','.join(d)
	sql = " insert into netease_mail (`user`,`pass`) values %s " % data
	return myConn.execute(sql)
	'''
	for i in body:
		if len(i)>2:
			i[0] = i[0].replace(' ', '')
			i[1] = i[1].replace(' ', '')
			try:
				myConn.execute(" insert into `netease_mail_%s` (`mail`,`pass`,`note`) values (%s, %s, %s) ", int(num), i[0], i[1], i[2])
			except:
				pass
	return len(body)

if __name__=='__main__':
	get_txt_list(path_)






