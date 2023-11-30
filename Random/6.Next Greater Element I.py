#    Author : Mohamed Yousef 
#    Date   : 2022-12-07
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
def solve(nums1,nums2):
    n=len(nums2)
    ans=[-1]*n
    out=[]
    stack=deque()
    for i in range(n):
        while stack and nums2[i]>nums2[stack[-1]]:
            ans[stack[-1]]+=i+1
            del stack[-1]
        stack.append(i)
    # return ans
    for i in nums1:
        x=ans[nums2.index(i)]
        if x==-1:
            out.append(x)
        else:out.append(nums2[x])
    return out

print(solve([2,4],[1,2,3,4]))