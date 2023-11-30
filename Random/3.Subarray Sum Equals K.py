#    Author : Mohamed Yousef 
#    Date   : 2023-01-04
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def solve(nums,k):
    myDict=defaultdict(int)
    myDict[0]+=1
    sum=0
    ans=0
    for i in nums:
        sum+=i
        store=sum-k
        if store in myDict:
            ans+=myDict[store]
        myDict[sum]+=1
    return ans

print(solve([1,2,3],3))
