# -*- coding: utf-8 -*-
import time
import datetime #获取毫秒数
"""
 各种排序
"""

"""
冒泡排序
两两相邻对比，判断大小，并换位置 ，每一轮完后都会把最大的放最后面
时间复杂度 n*n   表达式 o(n²)    
"""
def getPao(arr):
	for i in range (1, len(arr)): #需要冒泡的轮数
		#print "%s 轮" %(i)
		for k in range(0, len(arr)-i): #每轮冒出一个数 需要比较的次数
			#print "%s : %s" %(arr[k], arr[k+1])
			if arr[k] > arr[k+1] :
				tmp = arr[k]
				arr[k] = arr[k+1]
				arr[k+1] = tmp
	return arr
arr = [1,43,54,62,21,66,32,78,36,76,39]
print "冒泡排序法"
print "start:%s" %(datetime.datetime.now())
arr1 = getPao(arr)
print "==end:%s" %(datetime.datetime.now())
print arr1


"""
选择排序法
没次选择一个相应的元素，将其放到指定位置
双重循环完成，外层控制轮数，当前的最小值。内层 空海比较次数
对每一个值，依次对比其后面的所有值 取最小放在前面
时间复杂度 n+(n-1)+(n-2)+..... 
"""
def select_sort(arr):
	for i in range(0, len(arr)-1): #i当前最小值的位置
		p = i #先假设最小值的位置
		#print "%s 轮" %(p)
		for j in range (i+1, len(arr)): #j当前需要和哪些元素进行比较，i后边的全部
			#print " %s : %s" %(arr[p], arr[j])
			if arr[p] > arr[j]: # arr[p]是 当前已知的最小值，如果发现更小的，记录下最小时的位置，并且在下次比较时
				p = j		
		if p != i: #已经确定了当前的最小值的位置，保存到p中，如果发现最小的位置与当前假设的位置i不同 则互换
			tmp = arr[p]
			arr[p] = arr[i]
			arr[i] = tmp
		#print arr
	return arr
#简化实现2
def select_sort2(arr):
	for i in range(0, len(arr)-1):
		for j in range(i, len(arr)):
			if arr[i] > arr[j]:
				temp = arr[i]
				arr[i] = arr[j]
				arr[j] = temp
	return arr
arr = [1,43,54,62,21,66,32,78,36,76,39]
print "选择排序法"
print "start:%s" %(datetime.datetime.now())
arr1 = select_sort2(arr)
print "==end:%s" %(datetime.datetime.now())
print arr1

"""
插入排序法
"""
def instert_sort(arr):
	for i in range(1, len(arr)):
		tmp = arr[i]
		for j in range(i-1, 0, -1):
			if tmp < arr[j]:
				arr[j+1] = arr[j]
				arr[j] = tmp
			else:
				break
	return arr
arr = [1,43,54,62,21,66,32,78,36,76,39]
print "插入排序法"
print "start:%s" %(datetime.datetime.now())
arr1 = instert_sort(arr)
print "==end:%s" %(datetime.datetime.now())
print arr1


"""
快速排序法(二分法)
(递归)
将list第一个元素作为标尺，其余所有元素跟标尺对比大小
"""
def quick_sort(arr):
	if len(arr) <= 1: #判断是否需要继续进行排序
		return arr
	base_num = arr[0] #选中一个标尺，第一个元素
	
	left_arr = [] #小于标尺的
	right_arr= [] #大于标尺的
	for i in range(1, len(arr)): #遍历除了标尺外的所有元素
		if base_num > arr[i]:
			left_arr.append(arr[i])  #小于 ：放左边
		else:
			right_arr.append(arr[i]) #大于 ：放右边
	#再分别对 左边 和 右边 的数组进行相同的排序处理方式（递归）
	left_arr = quick_sort(left_arr)
	right_arr= quick_sort(right_arr)
	
	#合并list
	left_arr.extend([base_num])
	left_arr.extend(right_arr)
	return left_arr
arr = [1,43,54,62,21,66,32,78,36,76,39]
print "快速排序"
print "start:%s" %(datetime.datetime.now())
arr1 = select_sort2(arr)
print "==end:%s" %(datetime.datetime.now())
print arr1




