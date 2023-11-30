#    Author : Mohamed Yousef 
#    Date   : 2023-02-08
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

class Solution:
    def solve(self,nums):
        n=len(nums)
        if n==1:return 0
        jumbNum=1
        curr=nums[0]
        Max=nums[0]
        for i in range(n-1):
            # print(type(curr),type(n-1))
            if curr>=n-1:
                return jumbNum
            Max=max(Max,i+nums[i])
            if i==curr:
                jumbNum+=1
                curr=Max
        return jumbNum

solve=Solution()
print(solve.solve([2,3,0,1,4]))

