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

t = test()
for _ in range(t):
    n = test()
    l = lvalues()
    result = []
    for i in range(n - 1):
        l[i + 1] = l[i] * l[i + 1]
        result.append(1)
    result.append(l[-1])
    print(sum(result) * 2022)