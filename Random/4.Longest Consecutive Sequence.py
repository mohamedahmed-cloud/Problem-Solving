#    Author : Mohamed Yousef 
#    Date   : 2022-12-15
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def solve(nums):
    numSet=set(nums)
    longest=0
    for n in numSet:
        if n-1 not in numSet:
            length=0
            while n+length in numSet:
                length+=1
            longest=max(longest,length)
    return longest

print(solve([0,3,7,2,5,8,4,6,0,1]))