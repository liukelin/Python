#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 测试使用 redis 的 incr 生成唯一ID
#  python 多线程模拟并发 (QPS以秒为单位， 不考虑 python GIL)
#  @author:  liukelin 314566990@qq.com
#
import redis
import time
import threading
import MySQLdb

redis_conf = {
        'default':{
             'host': '127.0.0.1',
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
        }
    }

#
# 使用redis incr生产唯一ID
#
def new_pid(r,key):
    pid = 0
    try :
        pid = r.incr(key)
    except:
        pool = redis.ConnectionPool(**redis_conf['default'])
        r = redis.Redis(connection_pool=pool)
        pid = r.incr(key)
    return pid if pid else 0

#
# 批量入库
#
def set_pid_batch(olist):
    ret = 0
    if len(olist) <= 0 :
        return ret
    sql = ''
    for i in olist:
        if i['pid'] == 0:
            pass
        sql += "(%s,%s,%s)," % ( i['pid'], i['time'], i['threadNum'])
    if sql == '':
        return ret

    sql = " insert into k_user(`uid`,`time`,`thread`) values %s " % sql[:-1]
    # print sql

    db = db_conf['default']
    conn = MySQLdb.connect(
        host        = db['host'],
        user        = db['user'],
        passwd  = db['passwd'],
        db           = db['db'],
        port        = db['port'],
        charset   = db['charset']
    )
    cur = conn.cursor()
    ret = cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()
    return ret

'''
#
# 入库
#
def set_pid(pid , threadNum=0 ):
    db = db_conf['default']
    conn = MySQLdb.connect(
        host        = db['host'],
        user        = db['user'],
        passwd  = db['passwd'],
        db           = db['db'],
        port        = db['port'],
        charset   = db['charset']
    )
    cur = conn.cursor()
    ret = cur.execute(" insert into k_user(`uid`,`time`,`thread`) values (%s,%s,%s)  ",(pid,  int(time.time()) , threadNum ))
    conn.commit()
    cur.close()
    conn.close()
    return ret
'''

#
# 执行
# threadNum 线程编号
# outTime  执行时间
#
def go(threadNum, outTime=60):
    pool = redis.ConnectionPool(**redis_conf['default'])
    r = redis.Redis(connection_pool=pool)

    start = int(time.time())
    data[threadNum] = []
    while 1:
        pid = new_pid(r,'pid')

        ret = 0
        # ret = set_pid(pid, threadNum)
        data[threadNum].append({'pid':pid, 'threadNum':threadNum , 'time':int(time.time()) }) #区分各线程变量
        if len(data[threadNum]) >= 5000: # 5千入库一次 
            ret = set_pid_batch(data[threadNum])
            data[threadNum] = []

        if (int(time.time()) - start) > outTime:
            ret = set_pid_batch(data[threadNum])
            data[threadNum] = []
            break

        print "==thread:%s==uid:%s==%s==" %(threadNum, pid, ret)
    return True

if __name__ == '__main__':
    outTime = 20  # 运行时间
    threadNo = 20 # 线程数

    data = {}
    threads = []
    for i in xrange(0, threadNo):
        t = threading.Thread(target=go, args=(i, outTime) )
        threads.append(t)

    for t in threads:
        t.setDaemon(True) #将线程声明为守护线程
        t.start()

    for t in threads: #等待所有线程完毕
        t.join()
    print "all over %s" % time.time()


'''
--
-- 数据库: `k_kelin`
--
-- 表的结构 `k_user`
--
CREATE TABLE IF NOT EXISTS `k_user` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `uid` int(10) NOT NULL,
  `time` int(10) NOT NULL,
  `thread` int(10) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `uid` (`uid`,`time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 AUTO_INCREMENT=1 ;


SELECT COUNT( id ) , `time`
FROM  `k_user` 
WHERE 1 
GROUP BY `time`
ORDER BY COUNT( id ) DESC 

测试结果 : 插入11000/s  生成ID不重复
'''