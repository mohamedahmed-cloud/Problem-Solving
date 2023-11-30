#    Author : Mohamed Yousef 
#    Date   : 2023-02-04
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
t=int(input())
for _ in range(t):
    n=int(input())
    l=lvalues()
    ans=sum(l)
    res=-10e9
    for i in range(n-1):
        l[i],l[i+1]=-l[i],-l[i+1]
        res=max(ans-(-l[i]-l[i+1])+(l[i]+l[i+1]),res)
        l[i+1]=-l[i+1]
    print(res)

    