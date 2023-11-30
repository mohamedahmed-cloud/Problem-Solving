#!/usr/bin/env python3
from typing import Optional, List

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        low, high = 1, 10**9
        def maxOps(max_divide):
            return sum((num -1) // max_divide for num in nums)

        while low < high:
            mid = (low + high) // 2
            if maxOps(mid) > maxOperations:
                low = mid + 1
            else:
                high = mid
        return low

slv = Solution()
nums = [9]
maxOperations = 2
print(slv.minimumSize(nums, maxOperations))
