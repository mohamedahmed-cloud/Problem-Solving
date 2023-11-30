#    Author : Mohamed Yousef 
#    Date   : 2023-01-06
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py

def solve(costs,coins):
    ans=0
    freq=[0]*(10**5+1)
    for i in costs:
        freq[i]+=1
    for i,value in enumerate(freq):
        # choose min betwen i*value and coins
        coins-=(i)*value
        if coins>=0:
            ans+=value
        else:
            coins+=i*value
            ans+=coins//i
            return ans
        if coins<0:break
    return max(0,ans)
print(solve([10,2,10,10,10,10,8,2,7,8],25))


