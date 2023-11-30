#!/usr/bin/env python3
from typing import Optional, List

from heapq import heapify, heappop, heappush
from collections import deque
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        changes = deque()

        for i in classes:
            x = round( -((i[0] + 1) / (i[1] + 1)) + (i[0] / i[1]),5)
            changes.append((x, i))
        changes = list(changes)
        heapify(changes)

        for i in range(extraStudents):
            x = changes[0][1][0]
            y = changes[0][1][1]
            add1 = [x+ 1, y + 1]
            add2= round( -((x + 2) / (y + 2)) + ((x + 1) / (y + 1)), 8 )
            changes[0] = (add2, add1)
            heappop(changes)
            heappush(changes, (add2, add1))

        n = 0
        ans = 0
        for i in changes:
            ans += (i[1][0] / i[1][1])
            n += 1

        return round(ans / n, 5)

cls = Solution()
classes = [[2,4],[3,9],[4,5],[2,10]]
extraStudents = 4
print(cls.maxAverageRatio(classes, extraStudents))
