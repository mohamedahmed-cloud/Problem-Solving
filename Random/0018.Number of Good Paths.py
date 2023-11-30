#    Author : Mohamed Yousef 
#    Date   : 2023-01-15
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
from math import comb
class Solution:
    def numberOfGoodPaths(self, vals, edges):
        UF = {}
        def find(x):
            UF.setdefault(x,x)
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        def union(x,y):
            UF[find(x)] = find(y)
        
        tree = defaultdict(list)
        val2Nodes = defaultdict(set)
        for s,e in edges:
            tree[s].append(e)
            tree[e].append(s)
            val2Nodes[vals[s]].add(s)
            val2Nodes[vals[e]].add(e)
        
        res = len(vals)
        
        for v in sorted(val2Nodes.keys()):
            
            for node in val2Nodes[v]:
                for nei in tree[node]:
                    if vals[nei] <= v:
                        union(node,nei)
            
            groupCount = defaultdict(int)
            for node in val2Nodes[v]:
                groupCount[find(node)] += 1
                
            for root in groupCount.keys():
                
                res += comb(groupCount[root],2)
                
        
        return res
solve=Solution()
print(solve.numberOfGoodPaths([1,3,2,1,3],[[0,1],[0,2],[2,3],[2,4]]))