#    Author : Mohamed Yousef 
#    Date   : 2023-12-14
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

sys.stdin = open('diamond.in', 'r')
sys.stdout = open('diamond.out', 'w')

n, k = mvalues()
ans = []
for i in range(n):
    ans.append(test())

ans.sort()
p1 = 0
p2 = 0
res = -1
while p1 < n and p2 < n:
    while p2 < n and ans[p2] - ans[p1] <= k:
        p2 += 1
    if p2 - p1 > res: res = p2 - p1
    p1 += 1
print(res)

