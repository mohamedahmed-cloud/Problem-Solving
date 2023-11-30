#    Author : Mohamed Yousef 
#    Date   : 2023-01-17
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
class Solution:
    def solve(self,s):
        ones=ans=0
        for i in s:
            if i=="1":
                ones+=1
            elif ones:
                ones-=1
                ans+=1
        return ans
        
solve=Solution()
print(solve.solve("00011110"))