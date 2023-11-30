#    Author : Mohamed Yousef 
#    Date   : 2023-01-28
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50) #To increase Recursion depth in py

class SummaryRanges:

    def __init__(self):
        self.numSet=set()

    def addNum(self, value: int) -> None:
        self.numSet.add(value)
    def getIntervals(self) -> List[List[int]]:
        l=list(sorted(self.numSet))
        i=0
        res=[]
        n=len(l)
        # print(l)
        while i<n:
            start=l[i]
            while i+1<n and l[i]+1 ==l[i+1]:
                i+=1
            res.append([start,l[i]])
            i+=1
        return res
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()




solve=Solution()
ele=["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
values=[[], [1], [], [3], [], [7], [], [2], [], [6], []]

