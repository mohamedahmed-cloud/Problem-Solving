#    Author : Mohamed Yousef 
#    Date   : 2022-12-14
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py
# Time complexity is O(n)
# Space complexity is O(n)
def solve(nums):
    n=len(nums)
    prefix=[1]+nums
    postfix=nums+[1]
    for i in range(1,n+1):
        prefix[i]*=prefix[i-1]
        postfix[-(i+1)]*=postfix[(-i)]
    print(prefix,postfix)
    ans=[0]*n
    for i in range(n):
        ans[i]=prefix[i]*postfix[i+1]
    return ans
print(solve([-1,1,0,-3,3]))
# Solution by O(n) time , O(1) Space
def solve2(nums):
    n=len(nums)
    ans=[1]*n
    pre=1
    for i in range(n):  
        ans[i]=pre
        pre=nums[i]*pre
    post=1
    for i in range(n-1,-1,-1):
        ans[i]*=post
        post=nums[i]*post
    print(ans)
print(solve2([-1,1,0,-3,3]))
