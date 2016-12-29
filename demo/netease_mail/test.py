#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016
# @author: liukelin
#
'''
test
'''

a = '130****0009@163.com'
b = '0130***@163.com'

a1 = a.split('@')
b1 = b.split('@')

print a1[0][-4:],b1[0][:-3]

ass = {}
ass = {
	'asa':1,
}
if len(ass)==0:
	print 111

print 6875974916%12