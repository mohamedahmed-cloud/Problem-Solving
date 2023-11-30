#    Author : Mohamed Yousef 
#    Date   : 2022-12-07
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
def solve(nums):
    n=len(nums)
    sum1=0
    sum2=sum(nums[1:])
    i=0
    for i in range(1,n):
        if sum1==sum2:
            return i-1
        # print(sum1,sum2)
        sum1+=nums[i-1]
        sum2-=nums[i]
    if sum1==sum2:
        return i
    return -1
print(solve([1,7,3,6,5,6])) 