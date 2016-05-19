#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: liukelin  314566990@qq.com
# test rabitmq client 生产队列数据
#
import pika

rabbitmq_host = '192.168.179.157'
rabbitmq_port = 5672
      
def test1():
	credentials = pika.PlainCredentials('guest', 'geust')
	#这里可以连接远程IP，请记得打开远程端口
	parameters = pika.ConnectionParameters(rabbitmq_host,rabbitmq_port,'/',credentials) 

	# 建立连接
	connection = pika.BlockingConnection(pika.ConnectionParameters(parameters))  
	# 创建channel
	channel = connection.channel()  
	# 创建queue
	channel.queue_declare(queue='test_queue2')


	# 发送消息到指定队列   
	channel.basic_publish(exchange='',
						routing_key='test_queue2',
						body='Hello World!')
	print("[x] Sent 'Hello World!'")

	connection.close()



if __name__ == "__main__":
	test1()