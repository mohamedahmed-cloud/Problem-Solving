#    Author : Mohamed Yousef 
#    Date   : 2023-01-05
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py
t=int(sys.stdin.readline())
for _ in range(t):
    n,k=map(int,sys.stdin.readline().split())
    arr=list(map(int,sys.stdin.readline().split()))
    iterate=1
    for i in arr:
        if i==iterate:
            iterate+=1
    ans=n-(iterate-1)
    if ans%k==0:
        print(ans//k)
    else:print(ans//k+1)