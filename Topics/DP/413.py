from typing import List
from collections import defaultdict
from functools import cache

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        differ = []
        ans = 0


        for i in range(1, n):
            differ.append(nums[i] - nums[i -1])
        prev = None
        cnt = 0
        for i in differ:
            if prev != i:
                prev = i
                ans += (cnt - 1) * cnt // 2
                cnt = 0
            prev = i
            cnt += 1
        ans += (cnt - 1) * cnt // 2

        return ans

slv = Solution()
nums = [1,2,3,8,9,10]
print(slv.numberOfArithmeticSlices(nums))


# another solution
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        ans = 0
        @cache
        def calculate(i):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] += dp[i - 1] + 1
            return dp[i]
        for i in range(2, n):
            ans += calculate(i)

        return ans

slv = Solution()
nums = [1,2,3,8,9,10]
print(slv.numberOfArithmeticSlices(nums))