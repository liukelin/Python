#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: liukelin  314566990@qq.com
# 多线程 抓取 图片
# 
import urllib3
import string
import re
import os
import time
import threading

dir_ = os.getcwd()

def set_logs(msg,file=''):
    # return
    logStr = "[%s]%s\r\n" %(time.strftime("%Y-%m-%d %H:%M:%S"),msg)
    file = file if file!='' else dir_
    f = open('%s/logs.log' % file,'a')
    f.write(logStr)
    f.close()

def get_img(url, page, dir , threadNum , threadNo=None):

    set_logs('开始抓取:%s.' % threadNo)

    #创建连接特定主机的连接池  
    # http_pool = urllib3.HTTPConnectionPool('wanimal1983.tumblr.com') 
    http = urllib3.PoolManager()

    k=0
    for i in page:
        k+=1

        if threadNo:
            if (k-1)%threadNum != threadNo: 
                continue

        findNum = 0 #匹配图片
        dowNum = 0 #保存图片

        # m = urllib.request.urlopen(url+str(i)).read() 
        # m = http_pool.urlopen('GET',url+str(i) ,redirect=False)
        try:
            r = http.request('GET', url)
        except:
            http = urllib3.PoolManager()
            r = http.request('GET', url)

        m = r.data
        # print(m)

        #创建目录保存每个网页上的图片  
        dirpath = dir
        '''
        dirname = str(i)  
        new_path = os.path.join(dirpath, dirname)  
        if not os.path.isdir(new_path):  
            os.makedirs(new_path)  
        '''
        page_data = m.decode('UTF-8')


        set_logs(page_data)

        page_image = re.compile('<img src=\"(.+?)\"')    #匹配img正则
        for image in page_image.findall(page_data): 

            print(image)
            pattern = re.compile(r'^http://.*$')  # 判断刷选图片
            if pattern.match(image):
                findNum += 1
                try: 
                    # print('start:')

                    image_name  = image.split("/")[-1] # get img name
                    image_path =  dirpath + '/'+ image_name

                    ret = 'fail'                    
                    if os.path.exists(image_path) == False:
                        # print ('1')
                        # image_data = urllib.request.urlopen(image).read() 
                        m2 = http.request('GET', image)
                        image_data = m2.data
                        
                        # print('2')
                        with open(image_path, 'wb') as image_file:  
                            image_file.write(image_data)  
                        image_file.close()
                        
                        ret = 'ok'
                        dowNum += 1
                        # print('3')
                    # print("%s:%s %s" %(time.strftime("%Y-%m-%d %H:%M:%S"),image_name,ret)) 
                except:  
                    print('Download failed')

        msg = "[%s]%s,查找:%s,保存:%s,thread:%s\r\n" %(time.strftime("%Y-%m-%d %H:%M:%S"),url+str(i),findNum,dowNum, threadNo)
        set_logs(msg,dir_)
        print(msg)



if __name__ == "__main__":

    urls ={
            'url' : 'http://www.chrismanstudios.com/',
            'dir' : '/Volumes/Liukelin/photos/www.chrismanstudios.com',



        }

    #statr page
    begin_page = 1
    # end page
    end_page = 10
    # 总线程数 
    threadNum = 10

    threads = []
    for i in range(0, threadNum):
        t = threading.Thread( target=get_img, name='get_img', args=(urls['url'], begin_page, end_page, urls['dir'], threadNum, i ) )
        threads.append(t)
    
    for t in threads:
        t.setDaemon(True)
        t.start()

    for t in threads:
        t.join()

    print('all over:%s' % time.strftime("%Y-%m-%d %H:%M:%S"))

