#    Author : Mohamed Yousef 
#    Date   : 2023-01-07
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py

def solve(gas,cost):
    n=len(cost)
    profit=0
    big=0
    start=-1
    for i in range(n):
        profit+=(gas[i]-cost[i])    
        big+=(gas[i]-cost[i])    
        if big<0:
            big=0
            start=i+1
    print(start)
    return -1 if profit<0 else start
print(solve([1,2,3,4,5], [3,4,5,1,2]))

