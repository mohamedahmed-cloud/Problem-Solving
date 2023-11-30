#    Author : Mohamed Yousef 
#    Date   : 2022-12-08
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque

n,t=map(int,sys.stdin.readline().split())
l=list(map(int,sys.stdin.readline().split()))
pointer2=0
sum1=0
all=0
ans=0
for i in range(n):
    sum1+=l[i]
    if sum1>t:
        sum1-=l[pointer2]
        pointer2+=1
        all-=1
    all+=1
    ans=max(all,ans)
print(ans)

    