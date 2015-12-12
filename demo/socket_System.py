#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket     #socket模块
import commands   #执行系统命令模块
import threading


HOST = '127.0.0.1'
PORT = 50007

"""
使用多线程 单个个Client
ip:num 作为编号
"""
def Client_threads():
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #定义socket类型，网络通信，TCP
		s.bind((HOST,PORT))   #套接字绑定的IP与端口
		s.listen(1)           #开始TCP监听（最多连接数量）
		while 1:
			conn,addr = s.accept() 
			while True:
				data = conn.recv(1024)    #把接收的数据实例化

				print data
				#conn.sendall(data)
				"""
				执行客户端输入的命令，在此执行为shell命令
				"""
				cmd_status,cmd_result = commands.getstatusoutput(data)   #commands.getstatusoutput执行系统命令（即shell命令），返回两个结果，第一个是状态，成功则为0，第二个是执行成功或失败的输出信息
				if len(cmd_result.strip()) == 0:   #如果输出结果长度为0，则告诉客户端完成。此用法针对于创建文件或目录，创建成功不会有输出信息
					conn.sendall('Done.')
				else:
					conn.sendall(cmd_result)   #否则就把结果发给对端（即客户端）
	except:
		print '连接错误'
	conn.close()  #关闭连接

if __name__ == '__main__':
    Client_threads()




