#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Client
"""
import socket
HOST = '192.168.179.130'  #127.0.0.1
PORT = 50007

try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #定义socket类型，网络通信，TCP
	s.connect((HOST,PORT))	#要连接的IP与端口
	while True:
		cmd = raw_input("Please input cmd:")	#与人交互，输入命令
		if cmd == '':
			continue
		s.sendall(cmd)	#把命令发送给对端
		data = s.recv(1024)	#把接收的数据定义为变量
		print data	#输出变量
except:
	print '连接失败'
finally:
	s.close()	#关闭连接