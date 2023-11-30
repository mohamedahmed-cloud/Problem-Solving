#    Author : Mohamed Yousef 
#    Date   : 2023-02-12
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())
class Solution:
    def solve(self,roads,seats):
        adj=defaultdict(list)
        for src,dst in roads:
            adj[src].append(dst)
            adj[dst].append(src)
        res=0
        # print(adj)
        def dfs(node,parent):
            nonlocal res
            passanger=0
            for child in adj[node]:
                if child!=parent:
                    p=dfs(child,node)
                    passanger+=p
                    res+=int(math.ceil(p/seats))
            return passanger+1
        dfs(0,-1)
        return res
solve=Solution()
print(solve.solve([[0,1],[0,2],[0,3]],3))