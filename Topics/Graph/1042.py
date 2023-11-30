#!/usr/bin/env python3
from typing import Optional, List
from collections import defaultdict

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        edges = defaultdict(set)
        ans = [0] * (n + 1)
        for node in paths:
            edges[node[0]].add(node[1])
            edges[node[1]].add(node[0])


        flowers = {1,2,3,4}

        for i in range(1, n + 1):
            token = {ans[node] for node in edges[i]}
            ans[i] = (flowers - token).pop()
        return ans[1:]

slv = Solution()
n = 5
paths = [[4,5],[4,3],[2,3],[3,5],[2,4]]
print(slv.gardenNoAdj(n, paths))