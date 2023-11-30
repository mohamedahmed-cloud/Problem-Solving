#    Author : Mohamed Yousef 
#    Date   : 2022-12-11
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
arr=[0,1,2,4,6,9,12,15,18,42]
def solve(arr,l,r,key):
    if l>r:return -1
    mid=(l+r)//2
    if arr[mid]==key:
        return mid
    elif arr[mid]>key:
        return solve(arr,l,mid-1,key)
    elif arr[mid]<key:
        return solve(arr,mid+1,r,key)
    return -1
print(solve(arr,0,len(arr)-1,1))
