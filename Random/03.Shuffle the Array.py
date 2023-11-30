#    Author : Mohamed Yousef 
#    Date   : 2023-02-06
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

class Solution:
    def solve(self,nums,n):
        ans=[0]*2*n
        x=n
        for i in range(0,n):
            ans[i*2]=nums[i]
            ans[i*2+1]=nums[i+x]
            
        return ans
solve=Solution()
print(solve.solve([2,5,1,3,4,7],3))

class Solution:
    def solve(self,nums,n):
        l1=nums[:n]
        l2=nums[n:]
        ans=deque()
        for i in range(n):
            ans.append(l1[i])
            ans.append(l2[i])
        return ans
solve=Solution()
print(solve.solve([2,5,1,3,4,7],3))
# solution three.
class Solution:
    def solve(self,nums,n):
        return chain(*zip(nums[:n],nums[n:]))
solve=Solution()
print(solve.solve())