#!/usr/bin/env python3

from typing import Optional, List
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        ans = [float("inf")] * n
        ans[src] = 0

        for i in range(k + 1):
            tmp = ans.copy()
            for u, v, w in flights:
                if ans[u] != float("inf") and ans[u] + w < tmp[v]:
                    tmp[v] = ans[u] + w
            ans = tmp.copy()

        return ans[dst] if ans[dst] != float("inf") else -1

slv = Solution()
n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 0
print(slv.findCheapestPrice(n, flights, src, dst, k))