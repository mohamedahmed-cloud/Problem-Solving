from typing import List
from collections import deque
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [nums[0]]
        ans = deque()
        for i in range(1, n):
            prefix.append(prefix[i - 1] + nums[i])

        summation = prefix[-1]

        for i in range(n):
            prev = 0
            next = 0
            prev = nums[i] * (i + 1 ) - prefix[i]

            if i <= n- 1:
                next = summation - prefix[i] - nums[i] * (n - i - 1)
        
            ans.append(prev + next)

        return ans

