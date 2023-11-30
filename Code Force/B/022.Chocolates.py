#    Author : Mohamed Yousef 
#    Date   : 2022-12-06
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
n=int(sys.stdin.readline())
l=list(map(int,sys.stdin.readline().split()))
ans=l[-1]
for i in range(n-2,-1,-1):
    x=min(l[i],l[i+1]-1)
    l[i]=x
    ans+=x
    if x<=1:break
print(ans)