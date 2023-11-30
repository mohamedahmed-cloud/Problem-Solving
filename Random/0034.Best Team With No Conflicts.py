#    Author : Mohamed Yousef 
#    Date   : 2023-01-31
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
class Solution:
    def solve(self,scores,ages):
        tab=[0]*(1+max(ages))
        scoresAges=sorted(zip(scores,ages))
        for s,a in scoresAges:
            tab[a]=s+max(tab[:a+1])
        return max(tab)

solve=Solution()
print(solve.solve([4,5,6,5],[2,1,2,1]))