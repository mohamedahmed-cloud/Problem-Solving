from typing import Optional, List
from heapq import heappop, heappush, heapify
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapify(stones)
        while len(stones) > 1:
            y = - heappop(stones)
            x = - heappop(stones)
            y -= x
            if y != 0:
                heappush(stones, -y)
            heapify(stones)
        if stones:
            return -stones[-1]
        else:
            return 0

slv = Solution()
print(slv.lastStoneWeight([1, 1, 5, 5]))