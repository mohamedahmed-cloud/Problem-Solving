#    Author : Mohamed Yousef 
#    Date   : 2023-01-20
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(5000) #To increase Recursion depth in py

class Solution:
    def solve(self,nums):
        ans=set() # we will use a set of tuple to prevent duplicate.
        n=len(nums)
        def backTrack(curr,add):
            if len(add)>1:
                ans.add(tuple(add))
            if curr==n:
                return
            if not add or add[-1]<=nums[curr]:
                backTrack(curr+1,add+[nums[curr]])
            backTrack(curr+1,add)
        backTrack(0,[])
        return ans

solve=Solution()
print(solve.solve([4,4,3,4,5]))
