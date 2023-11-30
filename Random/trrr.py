#    Author : Mohamed Yousef 
#    Date   : 2022-12-19
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py
t=int(sys.stdin.readline())
for _ in range(t):
    n,c=map(int,sys.stdin.readline().split())
    l=list(map(int,sys.stdin.readline().split()))
    for i in range(n):
        l[i]+=i+1
    l.sort()
    ans=0
    # print(l)
    for i in l:
        # print(c)
        c-=i
        if c>=0:
            ans+=1
        else:break
    print(ans)
