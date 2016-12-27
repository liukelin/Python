#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016
# @author: liukelin
#
'''
将文件 邮箱导 入redis
'''

import os
import sys
import time
import redis

file_check = ["txt"]#文件限制
config = {
	'redis':{
		'host': '192.168.1.86',
	    'port': 6379,
	    'db':0 
	}
}

# 
pool = redis.ConnectionPool(**config['redis'])
redisConn = redis.Redis(connection_pool=pool)

# 读取所有文件
def get_txt_list(path):
    try:
        #print "开始：%s" %(path)
        for i in os.listdir(path):
            temp_dir = os.path.join(path,i)
            if os.path.isdir(temp_dir):
                get_txt_list(temp_dir);
            else:
                if i.split('.')[-1].lower() in file_check:
                    # dirs[thread].append(temp_dir)
                    # shutil.copyfile(temp_dir,os.path.join(file_src,thread,i))
                    
                    # 读取文件
                    get_txt(temp_dir)
                                        
                    print "处理:%s" %(temp_dir)
    except:
        print 'Have no legal power' 
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
	        	d = line.split('----')
	        	if isinstance(d , (list)):
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
			print k, i
			redisConn.sadd(k, i)
		except:
			pass
	return len(data)



if __name__=='__main__':
	get_txt_list('/Volumes/LiukelinHD/网易裤子/52G葫芦娃/163com')

















