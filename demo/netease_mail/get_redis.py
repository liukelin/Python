#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2016
# @author: liukelin
#
'''
 从redis查找邮箱
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
# import pymysqls
# 
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

pool = redis.ConnectionPool(**config['redis'])
redisConn = redis.Redis(connection_pool=pool)

# 数据库连接实例
db.mysql = torndb.Connection(**config['mysql'])




















