from typing import List
from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:

        summation = 0
        ans = float("inf")
        mqueue = deque()

        for i, val in enumerate(nums):
            summation += val
            # cal k
            if summation >= k and ans > i + 1:
                ans = i + 1

            # shorten the size of mqueue
            curr = float("inf")
            while mqueue and summation - mqueue[0][0] >= k:
                curr = mqueue[0][1]
                mqueue.popleft()

            if curr != float("inf") and ans > i - curr:
                ans = i - curr

            # make it increasing sequence
            while mqueue and summation <= mqueue[-1][0]:
                mqueue.pop()

            mqueue.append((summation, i))
        return ans if ans != float("inf") else -1



slv = Solution()
nums = [2, 7, 3, -8, 4, 10]
k = 12
print(slv.shortestSubarray(nums, k))