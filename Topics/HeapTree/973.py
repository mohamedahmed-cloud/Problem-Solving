from typing import Optional, List
from heapq import heapify, heappop, heappush
from collections import deque
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        heapify(arr)
        n = 0

        for point in points:
            curr = point[0] ** 2 + point[1] ** 2
            if n < k:
                heappush(arr, [-curr, [point[0], point[1]]])
                n += 1
            elif -curr > arr[0][0]:
                heappop(arr)
                heappush(arr, [-curr, [point[0], point[1]]])
                
        return [x[1] for x in arr]
slv = Solution()
points = [[3,3],[5,-1],[-2,4]]
k = 2
print(slv.kClosest(points, k))

