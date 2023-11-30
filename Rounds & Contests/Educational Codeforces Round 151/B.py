#    Author : Mohamed Yousef 
#    Date   : 2023-07-03
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

for _ in range(test()):
    Ax, Ay = mvalues()
    Bx, By = mvalues()
    Cx, Cy = mvalues()
    d = 1

    AB = abs(Ax - Bx) + abs(Ay - By)
    AC = abs(Ax - Cx) + abs(Ay - Cy)
    BC = abs(Bx - Cx) + abs(By - Cy)

    d = 1 + ((AB + AC) - BC) //2
    print(d)
