#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import os
import datetime
import zipfile
'''
	修改zip （apk）文件注释
	使用 zipfile
'''
def file_zip():
	#开始压缩： 把空文件（empty）压缩到META-INF/uic_%s位置
    
    zipped = zipfile.ZipFile(path_shareapk, 'a', zipfile.ZIP_DEFLATED)
    filepath = "META-INF/uic_%s" % 'xxxx'
    zipped.write(path_empty, filepath)
    zipped.close()

def file_comment():
	# zipFile = zipfile.ZipFile(os.path.join(os.getcwd(), 'txt.zip'))
	zipFile = zipfile.ZipFile('/Users/liukelin/Downloads/mysql-slow.log')
	# zipInfo = zipFile.getinfo('/Users/liukelin/Downloads/mysql-slow.log')
	zipFile.comment('aaa')


if __name__=='__main__':
	file_comment()