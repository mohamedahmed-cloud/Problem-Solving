#    Author : Mohamed Yousef 
#    Date   : 2023-02-02
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
class Solution:
    def solve(self,arr):
        arr.sort()
        storeDict=defaultdict(int)
        for i in arr:
            storeDict[i]+=1
        for x,y in storeDict.items():
            need1=storeDict.get(x*2,-1)
            need2=storeDict.get(x/2,-1)
            need1=storeDict.get(x*2,-1)
            need2=storeDict.get(x/2,-1)
            if need2>=y:
                storeDict[x]=0
                storeDict[x/2]=need2-y
            elif need1>=y:
                storeDict[x]=0
                storeDict[x*2]=need1-y
            else:return False
        for x,y in storeDict.items():
            if y!=0:
                return False
        return True


solve=Solution()
print(solve.solve([-6,2,-6,4,-3,8,3,2,-2,6,1,-3,-4,-4,-8,4]))
