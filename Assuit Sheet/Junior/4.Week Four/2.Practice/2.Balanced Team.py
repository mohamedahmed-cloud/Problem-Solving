#    Author : Mohamed Yousef 
#    Date   : 2022-12-08
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
n=int(sys.stdin.readline())
l=list(map(int,sys.stdin.readline().split()))
l.sort()
pointer1=0
all=0
ans=0
for i in range(n):
    if l[i]-l[pointer1]>5:
        pointer1+=1
        all-=1
    all+=1
    ans=max(ans,all)
print(ans)