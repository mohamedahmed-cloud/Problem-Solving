#!/usr/bin/env python3

from typing import Optional, List
from collections import deque
from heapq import heapify, heappop, heappush
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        needed = [0] * n
        needed = deque(needed)
        for i in range(1, n):
            needed[i] =max(0, heights[i] -heights[i-1])

        i = 0
        token = []
        heapify(token)
        while ladders >= 0:
            while i < n and bricks >= needed[i]:
                heappush(token, -needed[i])
                bricks -= needed[i]
                i += 1

            if ladders > 0 and i < n:
                max_in_token = 0
                if token:
                    max_in_token = abs(token[0])
                we_toke = max(max_in_token, needed[i])

                if we_toke == max_in_token and token:
                    heappop(token)
                    bricks += we_toke
                else:
                    i += 1
            ladders -= 1
            
        return i - 1


heights = [4,12,2,7,3,18,20,3,19]
bricks = 10
ladders = 2
# heights = [4,2,7,6,9,14,12]
# bricks = 5
# ladders = 1
slv = Solution()
print(slv.furthestBuilding(heights, bricks, ladders))