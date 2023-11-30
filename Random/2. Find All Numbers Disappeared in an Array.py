#    Author : Mohamed Yousef 
#    Date   : 2022-12-10
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
# Solution With O(n) time and O(n) space.
def solve(nums):
    n=len(nums)
    freq=[0]*n
    # We can Replace deque with set data structure.
    ans=deque()
    for i in nums:
        freq[i-1]+=1
    for i in range(n):
        if freq[i]==0:
            ans.append(i+1)
    return list(ans)
print(solve([1,1]))
# Another Solution with O(n) time and O(1) space
def solve2(nums):
    # nums=deque(nums)
    for i in nums:
        index=abs(i)-1
        nums[index]=-abs(nums[index])
    res=deque()
    for i,value in enumerate(nums):
        if value>0:
            res.append(i+1)
    return list(res)
print(solve2([4,3,2,7,8,2,3,1]))

