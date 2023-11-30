#!/usr/bin/env python3
from collections import defaultdict
class Solution:
    def __init__(self):
        self.visited = set()
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        new_adj = defaultdict(list)
        ans = []
        for i in range(V):
            new_adj[i]= adj[i]

        def make_dfs(node, adj):
            self.visited.add(node)
            ans.append(node)
            for node in new_adj[node]:
                if node not in self.visited:
                    make_dfs(node, adj)
        make_dfs(0, new_adj)
        return " ".join(map(str,ans))
slv = Solution()
V = 4
adj = [[1,3], [2,0], [1], [0]]
print(slv.dfsOfGraph(V, adj))