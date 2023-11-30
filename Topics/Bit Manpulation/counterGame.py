#!/usr/bin/env python3

#    Author : Mohamed Yousef 
#    Date   : 2023-10-25
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

def is_power_of_two(num):
	return num > 0 and not (num & num - 1)
def lower_power_of_two(num):
	# print(num)
	while num > 0:
		if is_power_of_two(num):
			return num
		num -= 1

t = test()
for i in range(t):
	n = test()
	# print(n)
	iteration = 0
	while n != 1:
		if is_power_of_two(n):
			n //= 2
		else:
			n = lower_power_of_two(n)
		iteration += 1
	if iteration & 1:
		print("Richard")
	else:
		print("Louise")
	
