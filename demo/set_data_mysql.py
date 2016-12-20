#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016
# @author: liukelin
#
'''
test
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
# import common

config = {
	'mysql':{
		'host': '127.0.0.1',
	    'database': 'netease_mail', 
	    'user': 'root',
	    'password': '123456', 
	}
}

dir_ = ''
path_s = [
			'',
			'',
			'',
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
db.mysql = torndb.Connection(**config['mysql'])

file_check = ["txt"]#文件限制

# 读取所有文件
def get_txt_list(path, thread):
    try:
        #print "开始：%s" %(path)
        for i in os.listdir(path):
            temp_dir = os.path.join(path,i)
            if os.path.isdir(temp_dir):
                get_txt_list(temp_dir,thread);
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
		        	data.append(d)
		        	if i>0 and i%num==0:
		        		set_data(data)
		        		data = []
		        	i=i+1
	    else:  
	        break
	f.close()



# 批量入库
def set_data(body=[]):
	d = []
	for i in body:
		if i[0] and i[1]:
			msg = "(%s,'%s')" %(i[0],i[1])
			d.append(msg)
	data = ','.join(d)
	sql = " install into netease_mail (`user`,`pass`) values %s " % data
	return db.mysql.execute(sql)


if __name__=='__main__':
	get_txt_list(path_, 1)






