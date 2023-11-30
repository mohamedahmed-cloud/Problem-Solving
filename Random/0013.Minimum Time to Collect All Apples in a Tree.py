#    Author : Mohamed Yousef 
#    Date   : 2023-01-11
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py
class Solution:
    def solve(self,n,edges,hasApple):
        tree = defaultdict(list)
        for s,e in edges:
            tree[s].append(e)
            tree[e].append(s)
        print(tree)
        def dfs(node,par):
            res = 0
            for nei in tree[node]:
                if nei != par:
                    res += dfs(nei,node)
            if res or hasApple[node]:
                return res + 2
            return res
        return max(dfs(0,-1)-2, 0)



solve=Solution()
solve.solve(7,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],[False,False,True,False,True,True,False])