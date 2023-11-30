from typing import List
from heapq import heapify, heappop, heappush
from collections import deque

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        stack = []
        can_remove = n - k
        for i in range(n):
            # print(stack, nums[i], can_remove)
            while stack and nums[i] < stack[-1] and can_remove:
                # print("Enter")
                stack.pop()
                can_remove -= 1
            stack.append(nums[i])
        # print(can_remove)
        return stack[:k]
    
slv = Solution()
nums =nums = [2, 2, 2, 2]
k = 2
print(slv.mostCompetitive(nums, k))
