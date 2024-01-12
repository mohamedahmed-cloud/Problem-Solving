from typing import List
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        stack = []
        n = len(arr)
        for i in range(n):
            if not stack or  stack[-1] < arr[i]:
                stack.append(arr[i])
            else:
                indx = bisect_left(stack, arr[i])
                stack[indx] = arr[i]
        return len(stack)

slv = Solution()
nums = [10,9,2,5,3,7,101,18]
print(slv.lengthOfLIS(nums))

