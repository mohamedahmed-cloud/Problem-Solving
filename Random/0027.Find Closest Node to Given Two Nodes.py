#    Author : Mohamed Yousef 
#    Date   : 2023-01-25
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py

class Solution:
    def solve(self,edges,node1,node2):
        n=len(edges)
        INF=1e7
        l1=[INF for i in range(n)]
        l2=[INF for i in range(n)]
        def dfs(node,i,l):
            if l[node]>i:
                l[node]=i
                if edges[node]!=-1:
                    dfs(edges[node],i+1,l)
        dfs(node1,0,l1)
        dfs(node2,0,l2)
        # print(l1,l2)
        for i in range(n):
            l1[i]=max(l1[i],l2[i])
        ans=l1.index(min(l1))
        return ans if l1[ans]!=1e7 else -1



solve=Solution()
print(solve.solve([2,2,3,-1],0,1))
