#    Author : Mohamed Yousef 
#    Date   : 2023-01-16
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py

class Solution:
    def solve(self,intervals,newInterval):
        bisect.insort(intervals,newInterval)
        n=len(intervals)
        l=0
        while l<n-1:
            x=intervals[l]
            # print(intervals)
            # print(l)
            y=intervals[l+1]
            if x[1]>=y[0]:
                add=[min(x[0],y[0]),max(x[1],y[1])]
                intervals.remove(x)
                intervals.remove(y)
                intervals.insert(l,add)
                l-=1
                n-=1
            l+=1
            

        return intervals
        
solve=Solution()
print(solve.solve([[1,3],[6,9]] ,[2,5]))
