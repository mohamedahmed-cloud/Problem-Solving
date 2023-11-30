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

l = test()
r = test()
ans = -float("inf")
for i in range(l, r + 1):
	for j in range(l, r + 1):
		ans = max(ans, i ^j )
print(ans)
