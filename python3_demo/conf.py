#!/usr/bin/env python
# coding=utf-8
# @author: liukelin
import sys,os
import time

db_config = {
        #
        'default':{
            'host':'127.0.0.1',
            'port':3306,
            'user':'root',
            'passwd':'123456',#rootq1w2e3
            'db':'k_kelin',
            'charset':'utf8'
        },
    }
redis_conf = {
        'default':{
            'host':'127.0.0.1',
            'port':6379,
        }
    
    }

 #获取脚本路径
def cur_file_dir():
    path = sys.path[  0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)
 
#判断是否存在该进程
def check_process_num(processName) :
    if processName=='':
        return {"num":  3,"msg":"参数不正确"}
    temstr = 'ps -ef | grep "%s" | grep -v "grep" | wc -l' %(processName)
    output = os.popen(temstr)
    result =  int(output.read())
    if result ==   0:
        #print '进程不存在'
        return {"num":  0,"msg":"进程不存在"}
    else:
        #print '进程存在'
        return {"num":result,"msg":"进程存在"}