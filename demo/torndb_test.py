#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016
#
# @author: liukelin
# torndb是一个轻量级的基于MySQLdb封装的一个模块，其是tornado框架的一部分。
# 其项目主页为：https://github.com/bdarnell/torndb 。
# 从tornado3.0版本以后，其已经作为一个独立模块发行了。
# 可以通过 pip 或pip的方式直接安装。
# torndb对MySQLdb封装后，query,get返回是list,dict这些，非常方便，
# 可以直接拿来用，这是TA的优点，而且是默认自动commit的，不用MySQLdb的手动commit，用起来很是简洁。
# http://www.jb51.net/article/48827.htm
# 
# 解决
# EnvironmentError: mysql_config not found
# 首先查找mysql_config的位置，使用
# find / -name mysql_config ，比如我的在/usr/local/mysql/bin/mysql_config 将此 ls -s 到/usr/local/bin 下
# 
# 
# 解决python-mysql "Reason: image not found" 错误 http://blog.csdn.net/fenglvming/article/details/21124263
# sudo ln -s /usr/local/MySQL/lib/libmysqlclient.18.dylib /usr/lib/libmysqlclient.18.dylib
# 
# 
#
import torndb # python2依赖与MySQLdb (MySQL-python)  python3取消了MySQLdb使用PyMySQL
# print dir(torndb)
config = {
    'mysql':{
        'host': "127.0.0.1",
        'database': 'test',
        'user': 'root',
        'password': '',
        }
    }
myconn = torndb.Connection(**config['mysql'])
s = myconn.query(" select * from test1  ")
s1 = myconn.get(" select * from test2 limit 1 ")

print s,s1
