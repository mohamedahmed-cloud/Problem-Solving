#    Author : Mohamed Yousef 
#    Date   : 2022-12-18
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py
t=int(sys.stdin.readline())
for _ in range(t):
    n,p=list(map(int,sys.stdin.readline().split()))
    l=[1]*(n+1)
    ans=n
    for i in range(p):
        a,b=sorted(list(map(int,sys.stdin.readline().split())))
        l[b]=max(a+1,l[b])
    for i in range(1,n+1):
        l[i]=max(l[i-1],l[i])
        ans+=i-l[i]
    print(ans)