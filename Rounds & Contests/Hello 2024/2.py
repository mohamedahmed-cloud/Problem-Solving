#    Author : Mohamed Yousef 
#    Date   : 2024-01-06
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
    s = svalues()
    ans = 0
    skip = 0
    total = 0
    take = 0
    for i in range(n):
        if s[i] == "-":
            skip += 1
        else:
            take += 1
    total = n - min(take, skip) * 2
    print(total)
    

