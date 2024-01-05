#    Author : Mohamed Yousef 
#    Date   : 2023-12-24
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
    ans = 1
    firstNegative = float("inf")
    for i, val in enumerate(l):
        ans *= val
    if ans <= 0:
        print(0)
    else:
        print(1)
        print(1, 0)

