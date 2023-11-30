from typing import List
from functools import reduce
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        nums = set(nums)
        print(nums)
        def recursion(n):
            if n not in nums:
                return n
            return recursion(n - 1)
        return recursion(n)

slv = Solution()
l = [1, 2]
print(slv.missingNumber(l))