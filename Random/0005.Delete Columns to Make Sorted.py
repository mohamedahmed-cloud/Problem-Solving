#    Author : Mohamed Yousef 
#    Date   : 2023-01-03
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def solve(strs):
    n=len(strs)
    y=len(strs[0])
    ans=0
    for i in range(y):
        for j in range(n-1):
            if strs[j][i]>strs[j+1][i]:
                ans+=1
                break
    return ans

print(solve(["cba","daf","ghi"]))