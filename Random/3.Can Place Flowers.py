#    Author : Mohamed Yousef 
#    Date   : 2022-12-03
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
def solve(flower,n):
    x=len(flower)
    if x==1:
        if flower[0]==1:
            if n==0:return True
            return False
        return True
    if flower[0]==0 and flower[1]==0:
        flower[0]=1
        n-=1
    for i in range(1,x-1):
        if flower[i]==0 and flower[i+1]==0 and flower[i-1]==0:
            flower[i]=1
            n-=1
    if flower[-1]==0 and flower[-2]==0:
        flower[-1]=1
        n-=1
    if n<=0:return True
    return False

print(solve([1],0))