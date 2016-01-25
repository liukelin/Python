#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 测试使用 redis 的 incr 生成唯一ID
#  python 多线程模拟并发 (QPS以秒为单位， 不考虑 python GIL)
#  @author:  liukelin 31456690@qq.com
#
import redis
import time
import threading
import MySQLdb

redis_conf = {
        'default':{
             'host': "127.0.0.1",
             'port': 6379,
             'db': 0,
         }
    }
db_conf = {
        'default':{
            'host':'127.0.0.1',
            'port':3306,
            'user':'root',
            'passwd':'123456',
            'db':'k_kelin',
            'charset':'utf8'
        },
    }

#
# 使用redis incr生产唯一ID
#
def new_pid(r,key):
    # pool = redis.ConnectionPool(**redis_conf)
    # r = redis.Redis(connection_pool=pool)
    pid = r.incr(key)
    return pid if pid else 0

#
# 批量入库
#
def set_pid(db_conf, pid , threadNum=0 ):
    conn = MySQLdb.connect(
        host    = db_conf['host'],
        user    = db_conf['user'],
        passwd  = db_conf['passwd'],
        db      = db_conf['db'],
        port    = db_conf['port'],
        charset = db_conf['charset']
    )
    cur = conn.cursor()
    ret = cur.execute(" insert into k_user(`uid`,`time`,`thread`) values (%s,%s,%s)  ",(pid,  int(time.time()) , threadNum ))
    conn.commit()
    cur.close()
    conn.close()
    return ret

#
# 执行
# threadNum 线程编号
# outTime  执行时间
#
def go(threadNum, outTime=60):
    pool = redis.ConnectionPool(**redis_conf['default'])
    r = redis.Redis(connection_pool=pool)

    start = int(time.time())
    while 1:
        pid = new_pid(r,'pid')
        ret = set_pid(db_conf['default'], pid, threadNum )

        if (int(time.time()) - start) > outTime:
            break

        print "==%s==%s==%s==" %(threadNum, pid, ret)
    return True

if __name__ == '__main__':
    outTime = 20   # 执行时间
    threadNo = 20  # 线程数

    threads = []
    for i in xrange(0, threadNo):
        t = threading.Thread(target=go,args=(i,outTime) )
        threads.append(t)

    for t in threads:
        t.setDaemon(True) #将线程声明为守护线程
        t.start()

    for t in threads: #设在启动for外，等待所有线程完毕
        t.join()

    print "all over %s" % time.time()
