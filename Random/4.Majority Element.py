#    Author : Mohamed Yousef 
#    Date   : 2022-12-03
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
# very solw one see next solution it's a very creative solution 👌

def solve(nums):
    nums.sort()
    n=len(nums)
    maxelement=0
    repeated=1
    y=0
    x="i"
    for i in range(n-1):
        if nums[i]==nums[i+1]:
            repeated+=1
            y=nums[i]
        else:
            repeated=1
        if maxelement<repeated:
            x=y
            maxelement=repeated
    return x if x!="i" else nums[0]
print(solve([3]))

# Using Boyer-moore algorithm
def fast(nums):
    vote=0
    candidate=-1
    for i in nums:
        if vote==0:
            vote=1
            candidate=i
        else:
            if i==candidate:
                vote+=1
            else:
                vote-=1
    return candidate

print(fast([3]))
