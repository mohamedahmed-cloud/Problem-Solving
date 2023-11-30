from typing import List
from functools import reduce
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> int:
        n = len(nums)

        nums = set(nums)
        ans = set()
        print(nums)
        def recursion(n):
            if n <= 0:
                return ans
            if n not in nums:
                ans.add(n)
            return recursion(n - 1)
        return recursion(n)

slv = Solution()
l = [4,3,2,7,8,2,3,1]
print(slv.missingNumber(l))