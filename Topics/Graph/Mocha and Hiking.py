#    Author : Mohamed Yousef 
#    Date   : 2023-05-10
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

t = test()
for _ in range(t):
    n = test()
    l = lvalues()
    ans = list(range(1, n+1))
    for i in range(n + 1):
        if i == n or l[n-i-1] == 0:
            ans.insert(n-i, n + 1)
            break
    print(*ans)    
    