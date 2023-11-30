#    Author : Mohamed Yousef 
#    Date   : 2022-12-11
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
# Article in Meduim : https://medium.com/techie-delight/binary-search-practice-problems-4c856cd9f26c
nums = [8, 9,60, 1, 2, 3, 4, 5, 6, 7]
def solve(nums):
    n=len(nums)
    l,r=0,n-1
    while l<=r:
        if nums[l]<=nums[r]:
            return l
        mid=(l+r)//2
        next=(mid+1)%n
        prev=(mid-1+n)%n
        print(nums[l],nums[r],nums[mid])
        if nums[prev]>=nums[mid] and nums[next]>=nums[mid]:
            return mid
        elif nums[l]<=nums[mid]:
            # print(nums[l],nums[mid])
            l=mid+1
        elif nums[r]>=nums[mid]:
            r=mid-1
    return -1
print(solve(nums))

