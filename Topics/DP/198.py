from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)

        for i in range( n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return max(dp[n - 1], dp[n - 2])



slv = Solution()
nums = [1,7,9,2]
print(slv.rob(nums))