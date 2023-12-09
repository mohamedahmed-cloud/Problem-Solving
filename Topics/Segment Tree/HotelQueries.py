#    Author : Mohamed Yousef 
#    Date   : 2023-12-05
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

n, m = mvalues()
hotels = lvalues()
groups = lvalues()
seg = [0] * (4 * n)
def build(p = 1, s = 0, e = n - 1):
    if (s == e):
        seg[p] = hotels[s]
        return

    mid =  (s + e) // 2

    build(2 * p, s,mid )
    build(2 * p + 1, mid + 1, e)
    seg[p] = max(seg[2 * p], seg[2 * p + 1])

def update(val, p = 1, s = 0, e = n - 1):
    if s == e:
        seg[p] -= val
        print(f"{s + 1} ", end="")
    else:
        mid = (s + e) // 2
        if seg[2 * p] >= val:
            update(val, 2 * p, s, mid)
        else:
            update(val, 2 * p + 1, mid + 1, e)
        seg[p] = max(seg[2 * p], seg[2 * p + 1])

build()
for i in groups:
    if i > seg[1]:
        print("0 ", end=  "")
    else:
        update(i)
print()