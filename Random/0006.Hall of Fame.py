#    Author : Mohamed Yousef 
#    Date   : 2023-01-03
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def solve(n,strs):
    for i in range(n-1):
        ans=-1
        if strs[i]=="R" and strs[i+1]=="L":
            ans=0
            break
        elif strs[i]=="L" and strs[i+1]=="R":
            ans=i+1
            break
    return ans
    
for i in range(int(input())):
    print(solve(int(sys.stdin.readline()),sys.stdin.readline().strip()))