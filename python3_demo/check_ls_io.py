# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# liukelin
'''
生成测试文件
'''
import os
import threading
import time
import sys
import imp
import redis
imp.reload(sys)

dir_ = os.getcwd()
r = redis.Redis(host='localhost', port=6379, db=0)

def add_files():
	while 1:
		file = r.incr('test_key')
		f = open('%s/%s.log' % (dir_, file),'w')
		f.write(line)
		f.close()
		print('set %s' %file)


if __name__ == "__main__":

	# 总线程数 
    threadNum = 9

    threads = []
    for i in range(0, threadNum):
        t = threading.Thread( target=add_files, name='add_files', args=() )
        threads.append(t)
    
    for t in threads:
        t.setDaemon(True)
        t.start()

    for t in threads:
        t.join()

    print('all ok:%s' % time.strftime("%Y-%m-%d %H:%M:%S"))
