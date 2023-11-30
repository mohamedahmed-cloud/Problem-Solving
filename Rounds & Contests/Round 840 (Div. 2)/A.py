#    Author : Mohamed Yousef 
#    Date   : 2023-06-22
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
    Min = []
    Max = []
    for i in l:
        for j in l:
            Min.append(j & j)
            Max.append(i | j)
    x1 = l[0]
    x2 = l[0]
    for i in l:
        x1 &= i
        x2 |= i
    Max.append(x2)
    Min.append(x1)

    print(max(Max) - min(Min))

