#    Author : Mohamed Yousef 
#    Date   : 2022-12-06
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
n=int(sys.stdin.readline())
l=list(map(int,sys.stdin.readline().split()))
l.sort()
all=sum(l)
x=4.5*n-all
ans=0
if x<=0:
    ans=0
else:
    for i in l:
        x-=(5-i)
        ans+=1
        if x<=0:
            break
print(ans)