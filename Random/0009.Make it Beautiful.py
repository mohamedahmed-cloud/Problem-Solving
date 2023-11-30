#    Author : Mohamed Yousef 
#    Date   : 2023-01-08
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,sys.stdin.readline().split()))
    l1=set(l)
    check=False
    if len(l1)==1:
        print("NO")
        check=True
    else:
        l.sort()
        result=[]
        for i in range(n//2):
            result.append(l[i])
            result.append(l[-(i+1)])
        if n%2!=0:
            result.append(l[n//2])
    if not check:
        print("YES")
        print(*result)
