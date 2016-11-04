#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: liukelin  314566990@qq.com
# 基于 gevent 的 wsgi web服务器


import time
import gevent # 作为web服务器 
from gevent import monkey 
monkey.patch_all() #将程序转换成可以使用gevent框架的异步程序。

def echo1():
	print '1'

'''
	基于 gevent 的 wsgi web服务器
'''
def wsgi_server(address, port, app):
    server = gevent.wsgi.WSGIServer((address, port), app , log=None)
    gevent.signal(signal.SIGTERM, server.close)
    gevent.signal(signal.SIGINT, server.close)
    server.serve_forever()

'''
	方法2
'''
def server():
    from gevent.server import StreamServer
    server = StreamServer(('0.0.0.0', 6000), echo)
    print('startup... port:6000')
    server.server_forever()

def echo(socket, address):
    print('New')
    socket.sendall('welcome')
    fileobj = socket.makefile()
    while True:
        print 12


if __name__=='__main__':
    wsgi_server('0.0.0.0', 6000, echo1)