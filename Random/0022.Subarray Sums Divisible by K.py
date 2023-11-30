#    Author : Mohamed Yousef 
#    Date   : 2023-01-19
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py

class Solution:
    def solve(self,nums,k):
        mapped=defaultdict(int)
        mapped[0]=1
        ans=0
        sum=0
        for i in nums:
            sum+=i
            mod=sum%k
            ans+=mapped[mod]
            mapped[mod]+=1
        print(mapped)
        return ans

solve=Solution()
print(solve.solve([1,2,3,-3,3],3))