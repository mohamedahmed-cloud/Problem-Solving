#    Author : Mohamed Yousef 
#    Date   : 2022-12-18
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def solve(wall):  
    myDict=defaultdict(int)
    n=len(wall)
    for i in range(n):
        for j in range(len(wall[i])):
            if j>0:
                wall[i][j]+=wall[i][j-1]
            myDict[wall[i][j]]+=1
    ans=0
    for key,value in myDict.items():
        if wall[0][-1]!=key:
            ans=max(value,ans)
    return n-ans
print(solve([[2],[2],[2]]))
