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
    ans = []
    for i in range(k):
        ans.append(i + 1)
    tmp = n
    for i in range(n - k - 1, -1, -1):
        ans.append(tmp)
        tmp -= 1
    print(*ans)
