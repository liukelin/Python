#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: liukelin  314566990@qq.com
# test rabitmq system 获取/消费队列数据
#
import pika
import config
import time

'''
 官方案
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

	# 是确保队列存在
	channel.queue_declare(queue=queue_name)

	def callback(ch, method, properties, body):
	    print(" [x] Received %r" % body)

	channel.basic_consume(callback,
	                      queue=queue_name,
	                      no_ack=True,         # 不需要ACK确认
	                     )

	print(' [*] Waiting for messages. To exit press CTRL+C')
	# 启动监听
	channel.start_consuming()


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

	channel.queue_declare(queue=queue_name, durable=True)
	print(' [*] Waiting for messages. To exit press CTRL+C')

	def callback(ch, method, properties, body):

		# 逻辑代码
	    print(" [x] Received %r" % (body,))
	    # time.sleep(1)
	    print(" [x] Done")

	    ch.basic_ack(delivery_tag = method.delivery_tag) # 手动ACK确认（未ACK则数据一直保存在Unacked并等待消费，当Unacked数量>=prefetch_count则卡住该消费端，等待消费）

	channel.basic_qos(prefetch_count=1) # 允许暂留Unacked 数量，（数据未basic_ack前 数据保存在Unacked允许的最大值）

	channel.basic_consume(callback,  # 使用回调方法方式（）
						queue=queue_name,
						#no_ack=True,      #失效basic_ack：意思消费读取数据的时候，True为不要ack,由程序后面手工ack (basic_ack未执行，不会阻塞消费)，如果为设置，消费数据如果未basic_ack 操作，就会阻塞等待消费成功
						)

	channel.start_consuming() # 持续监听

	# `rabbitmq`实现了消息均分的功能，通过设置`basic.qos`方法的`prefetch_count`来实现。它会告诉`rabbitmq`的生产者不要给一个消费者分配过多的任务，也就是说不要在消费者处理完成已经接收到的任务之前分配新的任务。


if __name__ == "__main__":
	Work_Queues()










