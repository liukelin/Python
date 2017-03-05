#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016
# @author: liukelin
#

import redis

'''
假设该商品有1000份
goods_num = 1000

开抢之前设定好一个1000个元素的 redis set集合 goods_set(每个元素为商品id（goods_id）)
 sadd goods_set [1000]

uid = 1
'''

# 查询该用户是否购买过
check = redis.incr('check_'+uid)
if check and check>=1:
    return '你已经抢购过了'

goods_id= redis.spop(goods_set)
if goods_id: # 抢购成功

    
    '''
     其他业务处理
    '''

    if business: # 业务处理成功：
        # 标记用户已经购买过
        redis.incr('check_'+uid)
    else: # 将抢购的商品归还
        redis.sadd(goods_set, goods_id)

else:
    return '商品不足'
    
