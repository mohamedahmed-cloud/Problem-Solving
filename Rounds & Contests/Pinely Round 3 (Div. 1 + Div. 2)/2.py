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
    n = test()
    l = lvalues()
    res = 2
    while True:
        save = set()
        for i in l:
            save.add(i % res)
        if len(save) == 2:
            print(res)
            break
        res *= 2
