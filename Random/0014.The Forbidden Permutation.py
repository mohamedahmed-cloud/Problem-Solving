#    Author : Mohamed Yousef 
#    Date   : 2023-02-05
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
for i in range(int(input())):
    n,m,d=mvalues()
    l1=lvalues()
    l2=lvalues()
    res=float("inf")
    dict1=defaultdict()
    for i,value in  enumerate(l1):
        dict1[value]=i
    for i in range(1,m):
        x=dict1.get(l2[i-1])
        y=dict1.get(l2[i])
        z=y-x
        if z<0 and y>x+d:
            res=0
            break
        else:
            first=d-z
            res=min(z,res)
            if (x+n-1-y)>first:
                res=min(res,first+1)
    print(max(res,0))



    
