# -*- coding: utf-8 -*-
"""
获取本机下所有图片并显示路径
"""
import sys,os
import json

img_arr = ["jpg","png","gid","bmp","png","psd"]

#获取脚本文件的当前路径
def cur_file_dir():
     #获取脚本路径
     path = sys.path[0]
     #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)

img_lists = []
"""
获取目录结构
"""
def list_dir(path, res):
	try:
		for i in os.listdir(path):
		    temp_dir = os.path.join(path,i)  
		    if os.path.isdir(temp_dir):  
		        temp = {'dir':temp_dir, 'child_dirs' : [] , 'files' : []}  
		        res['child_dirs'].append(list_dir(temp_dir, temp))  
		    else:	
		    	res['files'].append(i)
		    	#只获取图片
		    	if i.split('.')[-1].lower() in img_arr :
		    		img_lists.append(temp_dir)
	except:
		print '无权限'
	return res
      
def get_config_dirs(dir):  
    res = {'dir':'root', 'child_dirs' : [] , 'files' : []}  
    return list_dir(dir,res)  

get_config_dirs('/')
# print img_lists
print "数量："+str(len(img_lists))
# print os.path.getsize('/Users/liukelin/Desktop/屏幕快照 2015-09-19 13.37.27.png')






