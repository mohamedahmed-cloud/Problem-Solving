#    Author : Mohamed Yousef 
#    Date   : 2022-12-11
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
def solve(nums,l,r,key):
    while l<=r:
        mid=(l+r)//2
        if nums[mid]==key:
            return mid
        elif nums[mid]<nums[r]:
            if nums[mid]<key<=nums[r]:
                l=mid+1
            else:r=mid-1
        else:
            if nums[l]<=key<nums[mid]:
                r=mid-1
            else:l=mid+1
    return -1
nums=[6,7,8,1,2,3,4]
print(solve(nums,0,len(nums)-1,8))