#python demo

# ========= pid_test.py =========

# 并发下唯一ID的生成规则 (python 多线程模拟并发 (QPS以秒为单位， 不考虑 python GIL))

# 1.的 incr （redis 为单线程, 原子性操作）

# 2.使用 mysql 表的唯一自增主键 (可用双实例/物理机 错开id(奇偶数))


# ========= /demo/get_all_image.py =========
# 多线程 获取本计算机下所有图片并保存

