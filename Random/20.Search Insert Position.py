#    Author : Mohamed Yousef 
#    Date   : 2023-02-21
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())
class Solution:
    def solve(self,nums,target):
        l,r=0,len(nums)-1
        def binarySearch(l,r):
            mid=0
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]<target:
                    l=mid+1
                else :
                    r=mid-1
            # or return r+1
            return l
        return binarySearch(l,r)       
solve=Solution()
print(solve.solve( [1,3,5,6] ,0))

class Solution:
    def solve(self,nums,target):
        return bisect.bisect_left(nums,target)



solve=Solution()
print(solve.solve([1,3,5,6] ,2))

