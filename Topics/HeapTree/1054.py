#!/usr/bin/env python3

from typing import Optional, List
from collections import Counter
from heapq import heapify, heappop, heappush, heapreplace
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count = Counter(barcodes)
        count = [[-u, v ]for v, u in count.items()]
        heapify(count)
        ans =[]
        curr = heappop(count)

        while count:
            ans.append(curr[1])
            curr[0] += 1
            curr = heapreplace(count, [curr[0], curr[1]]) if curr[0] < 0 else heappop(count)
        ans.append(curr[1])
        return ans
slv = Solution()
barcodes = [1,1,1,1,2,2,3,3]
print(slv.rearrangeBarcodes(barcodes))