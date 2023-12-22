from typing import List
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        mx = 0
        n = len(points)
        for i in range(1, n):
            tmp = points[i][0] - points[i - 1][0]
            if mx < tmp:
                mx = tmp
        return mx
