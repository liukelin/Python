 #-*- coding: utf-8 -*-
import threading #线程类

def test_fun(ThreadNum) :
	for i in range(1,101) :
		if (i%2) == (ThreadNum-1) :
			print "线程:%s : %s \r\n" %(str(ThreadNum) , str(i))


#数组
threads = []
#创建线程
t1 = threading.Thread(target=test_fun, args=(1,))
t2 = threading.Thread(target=test_fun, args=(2,))
threads.append(t1) #
threads.append(t2)

"""#开启守护线程 setDaemon(True)将线程声明为守护线程，必须在start() 方法调用之前设置，如果不设置为守护线程程序会被无限挂起。"""
for t in threads:
	t.setDaemon(True) 
	t.start() #启动线程
	
"""阻塞主进程 用于等待线程终止。join（）的作用是，在子线程完成运行之前，这个子线程的父线程将一直被阻塞。"""		
for t in threads:
	t.join()
	
exit("ok")
