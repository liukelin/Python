# -*- coding: utf-8 -*-
"""
 获取本机所有图片
 按盘分线程
"""
import os,sys
import shutil  #文件目录操作
import threading

dirs = {"C":[],"D":[],"E":[],"F":[]} #获取目录
#dirs = {"F":[]} #获取目录
file_src = 'F:/uploads' #防止目录
file_check = ["jpg","png","gif","bmp","psd","icon"]#文件限制

def get_img_list(path,thread):
    try:
        #print "开始：%s" %(path)
        for i in os.listdir(path):
            temp_dir = os.path.join(path,i)
            if os.path.isdir(temp_dir):
                get_img_list(temp_dir,thread);
            else:
                if i.split('.')[-1].lower() in file_check:
                        dirs[thread].append(temp_dir)
                        shutil.copyfile(temp_dir,os.path.join(file_src,thread,i))
                        print "线程:%s ,copy:%s" %(thread,temp_dir)
    except:
        print 'Have no legal power'
    return True

#get_img_list('E:','E')

#new 
threads = []
for k in dirs.keys():
    t = threading.Thread(target=get_img_list, args=(k+":/", k))
    threads.append(t)

#start
for t in threads:
    t.setDaemon(True)
    t.start()

#join
for t in threads:
    t.join()




for k in dirs.keys():
    print "%s : %s " %(k , len(dirs[k]))
exit('ok')




#print sys.path[0]
#print os.listdir('E:')

