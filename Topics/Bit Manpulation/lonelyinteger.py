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

m = test()
l = lvalues()
ans = 0
for i in l:
	ans ^= i
print(ans)