#    Author : Mohamed Yousef 
#    Date   : 2022-12-16
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def solve(nums):
    freq=[0]*3
    for n in nums:
        freq[n]+=1
    i=0
    for r in range(3):
        while freq[r]>0:
            nums[i]= r
            freq[r]-=1
            i+=1
    return nums
print(solve([2,0,1]))