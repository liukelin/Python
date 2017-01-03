# 将52G网易裤子，导入redis，进行查找

	set_mail_redis.py
	网上抓到一批带*邮箱（130****0000@163.com、xxxx***@163.com），需要进行碰撞匹配

	将52G邮箱导入redis，并匹配
	类型1手机邮箱：130****0000@163.com    [:3]+[-4:]为key    
	类型2普通邮箱：xxxx***@163.com		[:-3]为key  

	服务器内存才16G，所以分批 导入-匹配-flushdb。
	关闭redis rdb、aof 提高性能


13240051 line

delete from duobao_user_join  where id in (select id from (select  max(id) as id,count(id) as count_ from duobao_user_join group by msg having count_ >1 order by count_ desc) as tab )

SELECT * FROM information_schema.INNODB_TRX\G;

trx_mysql_thread_id