#    Author : Mohamed Yousef 
#    Date   : 2022-12-06
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
n,m=map(int,sys.stdin.readline().split())
x=max(n,m)
y=min(n,m)
z=x-y
ans=1
if z>=10:
    print(0)
else:
    for i in range(y+1,x+1):
        ans*=i
    print(str(ans)[-1])
