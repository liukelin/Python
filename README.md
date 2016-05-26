 == pid_test.py ==

 分布式并发下唯一ID的生成规则 (python 多线程模拟并发 ，QPS以秒为单位， 不考虑 python GIL)

 1.使用 redis 的 incr （redis 为单线程, 原子性操作）
	
	1.incr 操作即返回加1操作后的值，可直接使用。避免多操作而使用事务。
	
	2.持久性：只有一个key,可开启RDB/AOF，或者判断在nosql key失效时，获取DB表中最后一个生成的id并set写入，保持可持续使用。

	3.性能：内存操作，性能优良

	4.灾难恢复，数据自动恢复，脚本检测set进最后一个生成的ID

	redis> SET mykey "10"
	
	OK
	
	redis> INCR mykey
	
	(integer) 11
	
	redis> GET mykey
	
	"11"


 2.使用 mysql 表的唯一自增主键 (可用双实例/物理机 错开id(奇偶数 +1/+2))
	
	1.mysql的原子性，可保证自增列不会产生重复的id

	2.持久性：存在于mysql数据表中，持久化于磁盘

	3.性能：数据写入操作，可用错开id(+1/+2)双写



 == /demo/get_all_image.py ==
 多线程 获取本计算机下所有图片并保存


@author:  liukelin 31456690@qq.com
