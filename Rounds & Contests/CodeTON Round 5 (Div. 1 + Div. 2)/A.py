#    Author : Mohamed Yousef 
#    Date   : 2023-06-24
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

first = "Tenzing"
second = "Tsondu"
deal = "Draw"
t = test()
for _ in range(t):
    n,m = mvalues()
    x = sum(lvalues())
    y = sum(lvalues())
    if y < x:
        print(second)
    elif y > x:
        print(first)
    else:
        print(deal)