#!/usr/bin/env python3

from typing import Optional, List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time_needed = [float("inf")] * (n + 1)
        time_needed[k] = 0
        # times.sort()
        for i in range(4):
            for u, v, w in times:
                if time_needed[u] != float("inf") and time_needed[u] + w < time_needed[v]:
                    time_needed[v] = time_needed[u] + w
        # print(time_needed)
        ans = max(time_needed[1:])
        return ans if ans != float("inf") else -1




slv = Solution()
times = [[1,2,1],[2,3,7],[1,3,4],[2,1,2]]
n = 3
k = 2
print(slv.networkDelayTime(times, n, k))
