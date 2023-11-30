#    Author : Mohamed Yousef 
#    Date   : 2023-01-04
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def solve(tasks):
        myDict=defaultdict(int)
        ans=0
        for i in tasks:
            myDict[i]+=1
        # any answer after make any number%3 give me 2 or 1 
        # if give 1 we will increase in it 3 if num//3 more than 1 
        # if give 2 we will complete our compuation correclty.
        for key,value in myDict.items():
            if value<2:
                return -1
            store=value%3
            if store==0:
                ans+=value//3
            else:
                ans+=value//3
                ans+=1
                
        return ans

print(solve(tasks =
[69,65,62,64,70,68,69,67,60,65,69,62,65,65,61,66,68,61,65,63,60
,66,68,66,67,65,63,65,70,69,70,62,68,70,60,68,65,61,64,65,63,62,62,
62,67,62,62,61,66,69]))
