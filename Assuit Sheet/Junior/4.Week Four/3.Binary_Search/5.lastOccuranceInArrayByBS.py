#    Author : Mohamed Yousef 
#    Date   : 2022-12-11
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
def solve(nums,l,r,key):
    result=-1
    while l<=r:
        mid=(l+r)//2
        if nums[mid]==key:
            result=mid
            l=mid+1
        elif nums[mid]<key:
            l=mid+1
        else:r=mid-1
    return result
nums=[2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
print(solve(nums,0,len(nums)-1,9))