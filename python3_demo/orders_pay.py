#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016
# @author: liukelin
#
# 一个固定商品数量的抢购 的伪代码
# 1.避免抢购超出 预定数量
# 2.避免同用户多次抢购

import redis

'''
假设该商品有1000份
goods_num = 1000

开抢之前设定好一个1000个元素的 redis set集合 goods_set(每个元素为商品id（goods_id）)
 sadd goods_set [1 ，2 ，3 ，4 .. 1000]

uid = 1
'''

# 限制频繁请求
check_act = redis.incr('check_act'+uid)
if check_act>1:
    redis.ttl('check_act'+uid, 1)
    return '请求过于频繁，请稍后再试'


# 查询该用户是否抢购成功过
check = redis.incr('check_'+uid)
if check and check>=1:
    return '你已经抢购过了'

goods_id= redis.spop(goods_set)
if goods_id: # 抢购成功

    
    '''
     business 抢购成功业务处理
    '''

    if business: # 业务处理成功：
        # 标记用户已经购买过
        redis.incr('check_'+uid)
    else: # 将抢购的商品归还
        redis.sadd(goods_set, goods_id)

else:
    return '商品不足'
    
