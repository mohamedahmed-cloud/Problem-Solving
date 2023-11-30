#    Author : Mohamed Yousef 
#    Date   : 2023-11-18
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())


for _ in range(test()):
    n = test()
    l = lvalues()
    curr = 0
    ans = -float("inf")
    for i in range(1, n):
        if (l[i] % 2 == 0 and l[i - 1] % 2 == 1) or (l[i] % 2== 1 and l[i -1] % 2 == 0):
            curr += l[i] + l[i -1]
            ans = max(curr, ans)
        if curr  <= 0:
            curr = 0
    print(ans)