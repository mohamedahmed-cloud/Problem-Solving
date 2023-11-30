#    Author : Mohamed Yousef 
#    Date   : 2023-01-17
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py

class Solution:
    def solve(self,n):
        if n%4==0:
            return False
        return True
        # or another solution
        # return n%4



solve=Solution()
print(solve.solve(2))