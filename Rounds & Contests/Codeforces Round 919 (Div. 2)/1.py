#    Author : Mohamed Yousef 
#    Date   : 2024-01-13
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

for _ in range(test()):
    less = float("inf")
    large = 0
    notequal = set()
    for i in range(test()):
        a, val = mvalues()
        if a == 1:
            large = max(large, val)
        elif a == 2:
            less = min(less, val)
        else:
            notequal.add(val)
    ans = 0
    if less >= large:
        ans = abs(less - large) + 1
    # print(less, large, notequal)
    if ans:
        for i in notequal:
            if large <= i <= less:
                ans -= 1
    print(ans) if ans != float("inf") else print(0)
