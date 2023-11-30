#    Author : Mohamed Yousef 
#    Date   : 2023-01-28
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
# Bell Man Algorithm Tricky problem 😒
class Solution:
    def solve(self,n,flights,src ,dst,k ):
        dest=[float("inf")]*n
        dest[src]=0
        for i in range(k+1):
            temp=dest.copy()
            for u,v,w in flights:
                if dest[u]!=float("inf") and temp[v]>dest[u]+w:
                    temp[v]=dest[u]+w
            print(temp)
            dest=temp[:]
        print(dest)
        return dest[dst] if dest[dst]!=float("inf") else -1
solve=Solution()
print(solve.solve(4,[[0,1,1],[0,2,5],[1,2,1],[2,3,1]],0,  3,  1))
