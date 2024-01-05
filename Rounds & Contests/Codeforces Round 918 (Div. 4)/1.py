#    Author : Mohamed Yousef 
#    Date   : 2023-12-28
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

for _ in range(test()):
    l = lvalues()

    x = Counter(l)
    for i, val in x.items():
        if val == 1:
            print(i)
    # print(ans)
    