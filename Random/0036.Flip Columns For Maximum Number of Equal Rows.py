#    Author : Mohamed Yousef 
#    Date   : 2023-02-01
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py

class Solution:
    def solve(self,matrix):
        store=defaultdict(int)
        for x in matrix:
            add=[]
            for i in x:
                add.append(1-i)
            store[str(add)]+=1
            store[str(x)]+=1
        return max(store.values())
solve=Solution()
print(solve.solve([[0,0,0],[0,0,1],[1,1,0]]))
