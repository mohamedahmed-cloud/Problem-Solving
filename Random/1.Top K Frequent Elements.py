#    Author : Mohamed Yousef 
#    Date   : 2022-12-14
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def solve(nums , k):
    ourDict=defaultdict(int)
    for i in nums:
        ourDict[i] +=1
    ourDict=sorted(ourDict.items(),key=lambda ourDict:ourDict[1],reverse=True)
    # print(ourDict)
    ans=[]
    for i in range(k):
        ans.append(ourDict[i][0])
    return ans
print(solve([1,1,1,2,2,3], 2))
