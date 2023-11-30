#    Author : Mohamed Yousef 
#    Date   : 2022-12-06
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
n,k =map(int,sys.stdin.readline().split())
ans=0
if k==2:ans=0
elif n>k:
    n=k-1
    ans=n//2
elif n==k:
    ans=(k-1)//2
else:
    k//=2
    ans=n-k
    if ans<0:ans=0
print(ans)
