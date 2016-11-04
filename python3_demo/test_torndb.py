#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2016
#
# @author: liukelin
#
import torndb # 依赖与MySQLdb

config = {
    'mysql':{
        'host': "localhost",
        'database': 'duobao',
        'user': 'root',
        'password': '123456',
        }
    }
mysql = torndb.Connection(**config['mysql'])
s = mysql.query(" select * from goods  ")
print(s)