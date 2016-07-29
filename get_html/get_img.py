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
# import urllib

dir_ = os.getcwd() 

def set_logs(msg,file=''):
    logStr = "[%s]%s\r\n" %(time.strftime("%Y-%m-%d %H:%M:%S"),msg)
    file = file if file!='' else dir_
    f = open('%s/logs.log' % file,'a')
    f.write(logStr)
    f.close()

def get_img(url, begin_page, end_page, dir , threadNum , threadNo, headers={}):

    set_logs('开始抓取:%s.' % threadNo)

    #创建连接特定主机的连接池  
    # http_pool = urllib3.HTTPConnectionPool('wanimal1983.tumblr.com') 
    http = urllib3.PoolManager()

    # proxy_handler = urllib.request.ProxyHandler({'http':'52.79.97.212:64002'})  
    # proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()  
    # proxy_auth_handler.add_password('rc4-md5', '123.123.2123.123', 'user', 'qd123456**') 

    for i in range(begin_page, end_page + 1):

        if threadNo<1:
            if i%threadNum != threadNo: 
                continue

        findNum = 0 #匹配图片
        dowNum = 0 #保存图片

        # m = urllib.request.urlopen(url+str(i)).read() 
        # m = http_pool.urlopen('GET',url+str(i) ,redirect=False)
        try:
            r = http.request('GET', url+str(i))
        except:
            http = urllib3.PoolManager()
            r = http.request('GET', url+str(i))

        m = r.data
        # print(m)

        #创建目录保存每个网页上的图片  
        dirpath = dir
        '''
        dirname = str(i)  
        new_path = os.path.join(dirpath, dirname)  
        '''
        if not os.path.isdir(dirpath):  
            os.makedirs(dirpath)  
        
        page_data = m.decode('UTF-8') 
        # page_data = m.decode('GBK')
        page_image = re.compile('<img * src=\"(.+?)\"')    #匹配img正则

        for image in page_image.findall(page_data): 
            print(image)

            # pattern = re.compile(r'^http://.*.(jpg|png|gif|bmp)$')  # 判断刷选图片
            pattern = re.compile(r'^http://.*$')
            if pattern.match(image):
                findNum += 1

                # 保存图片的命名规则 
                image_name  = image.split("/")[-1] # 有.jpg结尾的
                # image_name = image.replace("/",'-')  # 无

                
                suffix = image_name.split(".")[-1] # 判断后最
                if (suffix not in ['jpg', 'png', 'gif', 'bmp']):
                    image_name += '.jpg'
                
                image_path =  dirpath + '/'+ image_name

                ret = 'fail'                    
                if os.path.exists(image_path) == False:

                    try:
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
                    except:  
                        print('Download failed')
                # print("%s:%s %s" %(time.strftime("%Y-%m-%d %H:%M:%S"),image_name,ret)) 
                

        msg = "%s,查找:%s,保存:%s,thread:%s\r\n" %(url+str(i),findNum,dowNum, threadNo)
        set_logs(msg,dir_)
        print(msg)



if __name__ == "__main__":

    # 抓取网址   
    # 保存位置
    urls = {
            # 'url' : "http://wanimal1983.tumblr.com/page/",
            'url' : "http://wanimal1983.org/page/",
            'dir' : '/Volumes/Liukelin/dowlod',

            # 'url' : "http://6taoke6.tumblr.com/page/",
            # 'dir' : '/Volumes/LiukelinHD/Photos/6taoke6',

            # 'url' : 'http://av66.tumblr.com/page/',
            # 'dir' : '/Volumes/LiukelinHD/Photos/av66',

            # 'url' : 'http://010feng.tumblr.com/page/',
            # 'dir' : '/Volumes/Liukelin/photos/010feng.tumblr.com',

            # 'url' : 'http://9mouth.lofter.com/?page=',
            # 'dir' : '/Volumes/Liukelin/photos/9mouth.lofter.com',

            # 'url' : 'http://www.huafox.com/?page=',
            # 'dir' : '/Volumes/Liukelin/photos/www.huafox.com',

            # 'url' : 'http://t.huafox.com/page/',
            # 'dir' : '/Volumes/Liukelin/photos/t.huafox.com',

            # 'url' : 'http://madebai.tumblr.com/page/',
            # 'dir' : '/Volumes/Liukelin/photos/madebai.tumblr.com',

            # 'url' : 'http://jasonzou.lofter.com/?page=',
            # 'dir' : '/Volumes/Liukelin/photos/jasonzou.lofter.com',

            
            # 'url' : 'http://www.chrismanstudios.com/ben-chrisman-wedding-photography-portfolio/',
            # 'url' : 'http://www.chrismanstudios.com/erin-chrisman-wedding-photography-portfolio/',
            # 'url' : 'http://www.chrismanstudios.com/mauricio-arias-wedding-photography-portfolio/',
            # 'url' : 'http://www.chrismanstudios.com/joseph-victor-stefanchik-wedding-photography-portfolio/',
            # 'url' : 'http://www.chrismanstudios.com/weddings-by-ryan/',
            # 'url' : 'http://www.chrismanstudios.com/chrisman-studios-best-wedding-videographers/vlad-chaloupka/',
            # 'dir' : '/Volumes/Liukelin/photos/www.chrismanstudios.com',

            # 'url' : 'http://weibo.com/p/1005051917322765/album?from=page_100505',
            # 'url' : 'http://www.moko.cc/post/141030.html',
            # 'url' : 'http://www.moko.cc/post/51279.html',
            # 'dir' : '/Volumes/Liukelin/photos/Arai-studio',

            # 'url'   : 'https://fashionshootexperience.wordpress.com/2015/01/07/creepy-fairytale-with-broncolor/',
            # 'dir'   : '/Volumes/Liukelin/photos/fashionshootexperience.wordpress.com'

        }

    #statr page
    begin_page = 1
    # end page
    end_page = 500
    # 总线程数 
    threadNum = 4

    headers = {
        # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        # 'Accept-Encoding' :'gzip, deflate',
        # 'Accept-Language' :'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Connection':'keep-alive',
        # 'Cookie':'JSESSIONID=CBE8F41CA2DB34CE41D8646D74BE2691; Hm_lvt_8d82e75c6168ba4bc0135a08edae2a2e=1461592136; Hm_lpvt_8d82e75c6168ba4bc0135a08edae2a2e=1461592165; LAST_LOGIN_EMAIL=314566990@qq.com; NEWMOKO_USER_LOGINKEY=aecef352-1f1c-483e-bc72-d70133f30884',
        # 'Host':'www.moko.cc',
        # 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:45.0) Gecko/20100101 Firefox/45.0'

        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        # 'Cookie':"""UOR=www.rr-sc.com,widget.weibo.com,login.sina.com.cn; SINAGLOBAL=7327243766231.557.1443019054913; ULV=1462456506504:20:1:1:863621642225.3728.1462456506456:1460096241335; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5yKSxwc65WvblJx9y9gGe75JpX5KMhUgL.Fozpeo.7SKz7S0-t; SUHB=0YhgWKDQUg-ll5; YF-Page-G0=1ac418838b431e81ff2d99457147068c; SUS=SID-2129052075-1462456497-GZ-3clnz-2a746f6ebd91181e3d68bcb72152e2b7; SUE=es%3D0f1a74236bef0de65e989d2008d55958%26ev%3Dv1%26es2%3Daedd950e0a08d691e213a2f9e89b3129%26rs0%3DSARJasgR0lgkKYzrpxYEMeWcl2VzPkkwCHL85c8JDjlNpdv0KgOO0ldkAUaGO9DV9BCU6hGnKXuscykvev8h7Jak4Hwi%252BYRWRCpt%252Fn3fQ%252BeuxwLj8%252FGC1%252FU9e%252Fg9SgOhlAvb8NHmaf6Fx3Yc43zea0UI51aMfwrFkjv49oa2MnU%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1462456497%26et%3D1462542897%26d%3Dc909%26i%3De2b7%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D2%26st%3D0%26uid%3D2129052075%26name%3D1037012585%2540qq.com%26nick%3Dkelin_Liu%26fmp%3D%26lcp%3D2015-08-15%252008%253A06%253A02; SUB=_2A256LyDhDeRxGeRP6VsR9SzMzDmIHXVZXRUprDV8PUNbvtBeLVrWkW9LHesXfcwsTw8XsfmytofYzHfGaGRPOA..; ALF=1493992496; SSOLoginState=1462456497; _s_tentry=login.sina.com.cn; Apache=863621642225.3728.1462456506456""",
        # 'Host':'weibo.com',
        # 'Referer':"""http://login.sina.com.cn/sso/login.php?url=http%3A%2F%2Fweibo.com%2Farai8282%3Fprofile_ftype%3D1%26is_pic%3D1&_rand=1462456496.453&gateway=1&service=miniblog&entry=miniblog&useticket=1&returntype=META&_client_version=0.6.16""",
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:45.0) Gecko/20100101 Firefox/45.0',

    }


    threads = []
    for i in range(0, threadNum):
        t = threading.Thread( target=get_img, name='get_img', args=(urls['url'], begin_page, end_page, urls['dir'], threadNum, i  ) )
        threads.append(t)
    
    for t in threads:
        t.setDaemon(True)
        t.start()

    for t in threads:
        t.join()

    print('all over:%s' % time.strftime("%Y-%m-%d %H:%M:%S"))

