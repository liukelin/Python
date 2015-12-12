#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
使用多线程，支持多个Client
ip:num 作为编号
"""

import socket     #socket模块
import commands   #执行系统命令模块
import threading

HOST = '192.168.179.130' # 127.0.0.1
PORT = 50007 #端口
listNum = 50 #支持最多线程数
timeOut = 500 #进程超时时间

def Client_threads(conn,addr):
	try:
		while True: #表示可持续接收Client
			if conn is None :
				break
			conn.settimeout(timeOut)	#超时时间
			data = conn.recv(1024)    #把接收的数据实例化
			
			#print "%s : %s : %s " %(conn, addr, data)
			msg = " echo %s : %s " %(addr, data,)
			conn.sendall(msg)
	except:
		print '连接断开'
	finally:
		conn.close()  #关闭连接

def main():
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #定义socket类型，网络通信，TCP
	s.bind((HOST,PORT))   #套接字绑定的IP与端口
	s.listen(listNum)           #开始TCP监听（设置最多连接数量）
	while 1:
		try :
			conn,addr = s.accept()   #接受TCP连接，并返回新的套接字与IP地址
			print "Connected by: %s" %(addr,)    #输出客户端的IP地址格式为元组('127.0.0.1', 50952)
			#while 1:
			thread = threading.Thread(target=Client_threads, args=(conn,addr))
			thread.setDaemon(True)
			thread.start()
		except:
			print '等待连接'
			break
		
    # conn.close()  #关闭连接

if __name__ == '__main__':
    main()




