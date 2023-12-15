#    Author : Mohamed Yousef 
#    Date   : 2023-12-05
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(str,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

# p = 1, s = 0, e = n -1  ===> fixed in all methods

def build(p, s, e):
    if s == e:
        seg[p] = 1
        return
    mid = (s + e) // 2
    build(2 * p, s, mid)
    build(2 * p + 1, mid + 1, e)
    seg[p] = seg[2 * p] + seg[2 * p + 1]


def update(p, s, e, indx):

    mid = (s + e) // 2
    if s == e:
        seg[p] = 0
        print(l[s], end = " ")
        return

    if indx <= seg[2 * p]:
        update(2 * p, s, mid, indx) #left
    else:
        update(2 * p + 1, mid + 1, e, indx - seg[2 * p]) # right

    seg[p] = seg[2 * p] + seg[2 * p + 1]

if __name__=="__main__":
    n = test()
    l = lvalues()
    seg = [0] * (8 * n)
    build(1, 0, n -1)
    query = lvalues()
    for i in query:
        update(1, 0, n - 1, i)
        print(seg)

