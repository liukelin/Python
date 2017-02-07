#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016
# @author: liukelin
#
'''
    去除mysql数据表中重复数据
    表数据太大，运行sql语句卡死线程。
    使用redis set集合排重 并入库
'''
import os
import time
import torndb
import redis

config = {
    'mysql':{
        'host': '127.0.0.1',
        'database': 'netease_mail', 
        'user': 'root',
        'password': '123456', 
    },
    'redis':{
        'host': '127.0.0.1',
        'port': 6379,
        'db':0 
    }
}

# 数据库连接实例
myConn = torndb.Connection(**config['mysql'])

pool = redis.ConnectionPool(**config['redis'])
redisConn = redis.Redis(connection_pool=pool)

def group_mail():
    page = 0
    limit = 5000000
    key = 'zset_group_mail'
    while True:
        page_ = page * limit
        olist = myConn.query(" select * from `duobao_user_join` limit %s,%s ", page_, limit)
        if not olist:
            break
        # zset = []
        for i in olist:
            val = "%s====%s" %(i['uid'], i['msg'])
            redisConn.sadd(key, val)
        page += 1
        print "page:%s. ok." % str(page)

    return True
        
if __name__=='__main__':
    group_mail()












