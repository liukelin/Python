#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016
# @author: liukelin
#
'''
将文件 邮箱导 入redis，并匹配
'''

import os
import sys
import time
import redis
import torndb
import db

file_check = ["txt"]#文件限制
config = {
	'mysql':{
		'host': '127.0.0.1',
	    'database': 'netease_mail', 
	    'user': 'root',
	    'password': '123456', 
	},

	'redis':{
		'host': '192.168.1.86',
	    'port': 6379,
	    'db':0 
	}
}

# 
pool = redis.ConnectionPool(**config['redis'])
redisConn = redis.Redis(connection_pool=pool)

db.mysql = torndb.Connection(**config['mysql'])


def logs(data):
	f = open('logs/log%s.log' % str(time.time()), 'w+')
	f.write(data)
	f.close()

# redis操作
def upredis(act, k, v):
	s = None
	try:
		if act =='smembers':
			s = redisConn.smembers(k)
		elif act=='sadd':
			redisConn.sadd(k, v)
		elif act=='flushdb':
			redisConn.flushdb()
	except:
		pool = redis.ConnectionPool(**config['redis'])
		redisConn = redis.Redis(connection_pool=pool)
		if act =='smembers':
			s = redisConn.smembers(k)
		elif act=='sadd':
			redisConn.sadd(k, v)
		elif act=='flushdb':
			redisConn.flushdb()
	return s


# 读取所有文件
def get_txt_list(path):
    
    logs("开始:%s, " %(path) )

    files = []
    try:
        # 获取文件总数
        for i in os.listdir(path):
            temp_dir = os.path.join(path,i)
            if os.path.isdir(temp_dir):
                get_txt_list(temp_dir);
            else:
                if i.split('.')[-1].lower() in file_check:
                    # dirs[thread].append(temp_dir)
                    # shutil.copyfile(temp_dir,os.path.join(file_src,thread,i))
                    
                    # get_txt(temp_dir)
                    files.append(temp_dir)

    except:
    	print 'Have no legal power' 

    logs("总文件数:%s \r\n" %(str(len(files)) ) )

    # 每个文件夹 分3次 导入 文件处理
    k = 0
    for i in files:
    	k += 1

    	print "处理:%s" %(temp_dir)
    	logs("处理文件:%s" %(str(k)) )
    	# 入库redis
    	get_txt(i)

    	if k==len(files) or k%(len(files)/3)==0:
        	# 匹配
        	get_duobao()

        	# 匹配指定邮箱
        	find_mails()
        	
        	# 清除redis
        	upredis('flushdb',0,0)
	        
    upredis('flushdb',0,0)
    logs("完成.\r\n")
    return True

# 读取内容
def get_txt(dir_):
	num = 5000 # 5000入库一次
	i = 0
	data = []
	f = open(dir_, "r")  
	while True:  
	    line = f.readline()  
	    if line:
	        line=line.strip()
	        if line:
	        	# d = line.split('----')
	        	# if isinstance(d , (list)):
	        	data.append(line)
	        	if i>0 and i%num==0:
	        		set_redis(data)
	        		data = []
	        	i=i+1
	    else:  
	        break
	f.close()

# 写入redis  list 结构
def set_redis(data):
	for i in data:
		try:
			d = i.split('@')
			k = d[0][:-3]
			# print k, i
			# redisConn.sadd(k, i)
			upredis('sadd', k, i)
		except:
			pass
	return len(data)

# 读取数据库数据，并匹配
def get_duobao():
	olist = db.mysql.query(" select * from `duobao_user` where `type_` in ('163.com', '126.com') ")
	for i in olist:
		try:
			d = i['mail'].split('@')
			k = d[0][:-3]
		except:
			continue

		try:
			# olist = redisConn.smembers(k)
			olist = upredis('smembers', k, 0)
			if olist:
				for i in olist
		except:
			continue
	return True

# 匹配是否存在问题
def find_mails():
	mails = [
			'gohacking@163.com',
			'sekift@163.com',
			'bingochen87@163.com',
			'bananamylove@163.com',
			'liukelin_1@163.com',
			'13763385134@163.com',
		]
	for i in mails:
		
		try:
			f = open('logs/'+i+'.log', 'w+')
			d = i.split('@')
			k = d[0][:-3]
			# olist = redisConn.smembers(k)
			olist = upredis('smembers', k, 0)
			if olist:
				for s in olist:
					f.write(s+"\r\n")

			f.close()
		except:
			continue


if __name__=='__main__':
	# 每个文件夹/  分2次导入redis，避免redis占满内存
	dirs = [
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
	for i in dirs:
		get_txt_list('' + i)



















