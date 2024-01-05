#    Author : Mohamed Yousef 
#    Date   : 2023-12-23
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

for _ in range(test()):
    direction = [0, 0, 0, 0]
    for i in range(test()):
        a, b = mvalues()
        if a > 0: direction[0] = 1
        elif a < 0: direction[1] = 1
        if b > 0: direction[2] = 1
        elif b < 0: direction[3] = 1
    
    if sum(direction) > 3: print("NO")
    else:print("YES")