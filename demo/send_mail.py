# -*- coding: UTF-8 -*-
'''
'''
import time
import smtplib  
from email.mime.text import MIMEText  
from email.header import Header

mailto_list=['314566990@qq.com'] 
mail_host="smtp.163.com"  #设置服务器
mail_user="liukelin_1"    #用户名
mail_pass="Liukelin1"   #口令 
mail_postfix="163.com"  #发件箱的后缀
  
def send_mail(to_list,sub,content):  
    me="make"+"<"+mail_user+"@"+mail_postfix+">"  
    msg = MIMEText(content,_subtype='plain',_charset='utf-8')  
    msg['Subject'] = Header(sub, 'utf-8') 
    msg['From'] = me
    msg['To'] = ";".join(to_list)  
    print msg['To']
    try:
        server = smtplib.SMTP()  
        server.connect(mail_host)  
        server.login('liukelin_1@163.com',mail_pass)  
        server.sendmail('liukelin_1@163.com', msg['To'], msg.as_string())  
        server.close()  
        return True  
    except Exception, e: 
        print str(e)  
        return False  
if __name__ == '__main__':  
    if send_mail(mailto_list,"makesssword", "hellow"):  
        print "发送成功"  
    else:  
        print "发送失败"