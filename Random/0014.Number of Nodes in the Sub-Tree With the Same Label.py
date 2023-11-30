#    Author : Mohamed Yousef 
#    Date   : 2023-01-12
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py

class Solution:
    def solve(self,n,edges,labels):
        tree = defaultdict(list)
        for s,e in edges:
            tree[s].append(e)
            tree[e].append(s)
        ans = [0] * n
        def dfs(node,parent):
            count=Counter()
            for nextNode in tree[node]:
                if nextNode!=parent:
                    count+=dfs(nextNode,node)
            count[labels[node]]+=1
            ans[node]=count[labels[node]]
            return count
        dfs(0,-1)
        return ans
        
        
solve=Solution()
print(solve.solve(7,[[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]],"aaabaaa"))