#!/usr/bin/env python
# coding=utf-8
# @author: liukelin
import MySQLdb
import sys
__all__ = ['MySQL']
class MySQL(object):
    '''
    MySQL
    '''
    conn = ''
    cursor = ''
    def __init__(self,host='localhost',user='root',passwd='root', db='mysql',port=3306 ,charset='utf8'):
       
        """MySQL Database initialization """
        try:
            self.conn = MySQLdb.connect(host,user,passwd,db,port,charset)
        except MySQLdb.Error,e:
            errormsg = 'Cannot connect to server\nERROR (%s): %s' %(e.args[0],e.args[1])
            print errormsg
            sys.exit()
           
        self.cursor = self.conn.cursor()
       
    def query(self,sql):
        """  Execute SQL statement """
        return self.cursor.execute(sql)
   
    def show(self):
        """ Return the results after executing SQL statement """
        return self.cursor.fetchall()
              
    def __del__(self):
        """ Terminate the connection """
        self.conn.close()
        self.cursor.close()

'''
#test
if __name__ == '__main__':
   
    mysql = MySQL(host=localhost,passwd='test',db='mysql')
    mysql.query('select * from users')
    result = mysql.show()
    print len(result)
    print result[1]

'''