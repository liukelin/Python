#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016
#
# @author: liukelin
#
import torndb # 依赖与MySQLdb
# print dir(torndb)
config = {
    'mysql':{
        'host': "192.168.1.86",
        'database': 'duobao',
        'user': 'canal',
        'password': 'canal',
        }
    }
myconn = torndb.Connection(**config['mysql'])
s = myconn.query(" select * from users  ")
s1 = myconn.get(" select * from users limit 1 ")

print s,s1
