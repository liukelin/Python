#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: liukelin  314566990@qq.com
# test rabitmq client 生产队列数据
#
import pika
import config
import time

'''
 官方案例"Hello World!"
'''
def test1():
	queue_name = 'test_queue3'

	credentials = pika.PlainCredentials(config.rabbitmq_user, config.rabbitmq_pass) # 远程访问禁止使用 guest账号
	#这里可以连接远程IP，请记得打开远程端口
	parameters = pika.ConnectionParameters(config.rabbitmq_host, config.rabbitmq_port,'/',credentials) 
	# 建立连接
	connection = pika.BlockingConnection(parameters) # 本机 parameters可直接写localhost
	# 创建channel
	channel = connection.channel()  

	# 是确保队列存在 / 创建queue
	channel.queue_declare(queue=queue_name)

	# 发送消息到指定队列   
	# channel.basic_publish(exchange='',
	# 					routing_key='test_queue3',
	# 					body='Hello World!')

	print("[x] Sent 'Hello World!'")
	for i in range(1,10000):
		channel.basic_publish(exchange='',
							routing_key=queue_name,
							body='test'+str(i))

	connection.close()


'''
 官方案例 Work Queues
 ACK 机制、队列持久化
'''
def Work_Queues():
	queue_name = 'test_queue1'

	credentials = pika.PlainCredentials(config.rabbitmq_user, config.rabbitmq_pass) # 远程访问禁止使用 guest账号
	#这里可以连接远程IP，请记得打开远程端口
	parameters = pika.ConnectionParameters(config.rabbitmq_host, config.rabbitmq_port,'/',credentials) 
	# 建立连接
	connection = pika.BlockingConnection(parameters) # 本机 parameters可直接写localhost
	# 创建channel
	channel = connection.channel()

	channel.queue_declare(queue=queue_name, durable=True) # durable=True 队列持久化（但是需要生产者和消费者同时设置持久化才能生效）

	for i in range(100):
	    message = ' Hello World!' + str(i)
	    channel.basic_publish(exchange='',
		    routing_key=queue_name,
		    body=message,
		    properties=pika.BasicProperties(delivery_mode = 2)) # 在消息发送时，需要指定`delivery_mode`来实现消息持久化：

	    print(" [x] Sent %r" % (message))
	    # time.sleep(1)
	connection.close()


if __name__ == "__main__":
	Work_Queues()













