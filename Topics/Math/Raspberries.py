#    Author : Mohamed Yousef 
#    Date   : 2023-12-08
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

for i in range(test()):
    n, k = mvalues()
    l = lvalues()
    mn = float("inf")
    search = set({2, 3, 5})
    def find():
        global mn
        for i in range(n):
            mod = l[i] % k
            if mod == 0:
                mn = 0
            mn = min(mn,  k - mod)
        return mn1
    
    if k in search:
        print(find())
    
    elif k == 1:
        print(0)
    elif k == 4:
        cnt = 0
        for i in range(n):
            if not l[i] % 2:
                cnt += 1
            if not l[i] % 4:
                cnt += 1
        print(min(max(0, 2 - cnt), find()))
    

