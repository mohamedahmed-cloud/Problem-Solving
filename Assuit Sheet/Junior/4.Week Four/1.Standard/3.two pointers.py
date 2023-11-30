#    Author : Mohamed Yousef 
#    Date   : 2022-12-10
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
n,m=map(int,sys.stdin.readline().split())
l=list(map(int,sys.stdin.readline().split()))
p1=0
p2=0
all=0
summation=0
ans=10e9
while p2<n:
    if summation>m:
        summation-=l[p1]
        p1+=1
        all-=1
        if summation>=m:
            ans=min(ans,all)
    else:
        summation+=l[p2]
        p2+=1
        all+=1
        if summation>=m:
            ans=min(ans,all)
if ans==10e9:
    print(-1)
    quit()
print(ans)
