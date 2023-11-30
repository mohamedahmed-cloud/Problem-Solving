#    Author : Mohamed Yousef 
#    Date   : 2023-01-30
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py

class Solution:
    def solve(self,n):
        res=[]
        def fib(n,memo):
            if n in memo:
                return memo[n]
            if n<=2:
                return min(n,1)
            else:
                memo[n]=fib(n-1,memo)+fib(n-2,memo)+fib(n-3,memo)
                res.append(memo[n])
                return memo[n]
        memo={}
        fib(n,memo)
        return res[-1]       



solve=Solution()
print(solve.solve(25))
