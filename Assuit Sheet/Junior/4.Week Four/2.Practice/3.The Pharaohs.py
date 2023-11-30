#    Author : Mohamed Yousef 
#    Date   : 2022-12-08
import sys,math,bisect,collections,itertools,heapq,time
from collections import defaultdict,deque
def binary_search(l,r):
    mid=(l+r)//2
    value=mid*(mid+1)//2
    if value==n:
        return mid
    elif value>n:
        return binary_search(l,mid-1)
    elif value<n:
        return binary_search(mid+1,r)
for i in range(int(input())):
    n=int(sys.stdin.readline())
    print(binary_search(0,n))

