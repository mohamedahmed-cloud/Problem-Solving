#    Author : Mohamed Yousef 
#    Date   : 2022-12-11
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
# Article in meduim : https://medium.com/techie-delight/top-7-greedy-algorithm-problems-3885feaf9430
def solve(nums):
    # Sort according to finish time.
    nums=sorted(nums,key=lambda x:x[1])
    selected=-1
    ans=0
    l=deque()
    for i in nums:
        if i[0]>=selected:
            l.append(i)
            selected=i[1]
            ans+=1
    return ans,l

print(solve([(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9),(6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]))