#    Author : Mohamed Yousef 
#    Date   : 2023-06-27
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())


for _ in range(test()):
    n, k = mvalues()
    l = lvalues()
    ans = 0
    curr = 1
    for i in l:
        if i == curr:
            ans += 1
            curr += 1
    
    notSorted = n - ans
    print(math.ceil(notSorted / k))
