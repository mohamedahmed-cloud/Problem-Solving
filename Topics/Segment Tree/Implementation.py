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
        seg[p] = arr[s]
        return

    build(2 * p, s, (s + e) // 2)
    build(2 * p + 1, (s + e) // 2 + 1, e)
    seg[p] = min(seg[ 2 * p], seg[2 * p + 1])

def update(p, s, e, indx, val):
    if s == e:
        seg[p] = val
        return

    if indx <= (s + e) // 2:
        update(2 * p, s, (s + e) // 2, indx, val) #left
    else:
        update(2 * p + 1, (s + e) // 2 + 1, e, indx, val) # right

    seg[p] = min(seg[2 * p], seg[2 * p + 1])

def get(p, s, e, r1, r2):
    if s >= r1 and e <= r2:
        return seg[p]
    if s > r2 or e < r1:
        return float("inf")
    return min(get(2 * p, s, (s + e) // 2, r1, r2), get(2 * p + 1, (s + e) // 2 + 1, e, r1, r2))



if __name__=="__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    n = len(arr)
    seg = [0] * 4 * n
    build(1, 0, n -1)
    print(seg)
    update(1, 0, n -1, 3, 10)
    print(seg)
    print(get(0, 0, n -1, 1, 6))
    

