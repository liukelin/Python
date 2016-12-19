#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2016
#
# @author: liukelin
#
import zipfile
import os

def file_comment():
	# zipFile = zipfile.ZipFile(os.path.join(os.getcwd(), 'txt.zip'))
	# zipFile = zipfile.ZipFile('/Users/liukelin/Downloads/swoole-framework-master.zip')
	# # zipInfo = zipfile.getinfo('/Users/liukelin/Downloads/swoole-framework-master.zip')
	# zipFile.comment = 'aaa'
	# 
	test = 'test'
	root_shareapk = "/Users/liukelin/Downloads/"
	path_seed = "/Users/liukelin/Downloads/QianDeerDuoBao_default_v1.0.0_20161212093056.apk"
	path_shareapk = "/Users/liukelin/Downloads/test/"
	# 先复制一份拷贝, 等待被压缩处理
	from shutil import copy
	copy(path_seed, path_shareapk)

	# 准备一个空文件empty, 没有则新建
	path_empty = os.path.join(root_shareapk, "empty")
	if not os.path.exists(path_empty):
		fp = open(path_empty, "w+")
		fp.close()
	#开始压缩： 把空文件（empty）压缩到META-INF/uic_%s位置
	# import zipfile
	zipped = zipfile.ZipFile(path_shareapk, 'a', zipfile.ZIP_DEFLATED)
	filepath = "META-INF/uic_%s" % test
	zipped.write(path_empty, filepath)
	zipped.close()



if __name__ == '__main__':
	file_comment()