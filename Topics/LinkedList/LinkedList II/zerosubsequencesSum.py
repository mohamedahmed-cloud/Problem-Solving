#    Author : Mohamed Yousef 
#    Date   : 2023-06-23
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())
arr = [-1, 2, -2,7,3,2,-5, 1,-1,1,1]
n = len(arr)
ans = []
s = set()
ps = 0
cnt = 0
for i in arr:
    ps += i
    if ps in s:
        cnt += 1
    s.add(ps)
print(cnt)

