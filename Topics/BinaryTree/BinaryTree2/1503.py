from typing import Optional, List

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(n - min(right) if right else 0, max(left)
        if left else 0)

slv = Solution()
n = 4
left = [4,3]
right = [0,1]
print(slv.getLastMoment(n, left, right))
