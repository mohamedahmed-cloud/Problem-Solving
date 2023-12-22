#    Author : Mohamed Yousef 
#    Date   : 2023-12-19
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

for _ in range(test()):
    n, k = mvalues()
    a = lvalues()
    b = lvalues()
    ans = 0
    tmp = 0
    mx = 0
    for i in range(min(n, k)):
        mx = max(b[i], mx)
        tmp += a[i]
        ans = max(ans, tmp + (k - i - 1) * mx)
    print(ans)
