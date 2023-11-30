#    Author : Mohamed Yousef 
#    Date   : 2023-01-23
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py


class Solution:
    def solve(self,n,trust):
        trustYes=[0]*1001
        trustNo=[0]*1001
        ans=-1
        ind=-1
        for i,j in trust:
            trustYes[i]=i
            trustNo[j]+=j
        for i in range(1001):
            if trustNo[i] and not trustYes[i]:
                    ans=trustNo[i]
                    ind=i
                    break
        if n-1 and ans//(n-1)==ind:
            return ind
        if n==1 :return 1
        return -1


        



solve=Solution()
print(solve.solve(1,[]))