from typing import List
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = -float("inf")
        n = len(nums)
        for i in range(n // 2):
            if ans < nums[-i - 1] + nums[i]: 
                ans =  nums[-i - 1] + nums[i]
        return ans

slv = Solution()
nums = [3,5,2,3]
print(slv.minPairSum(nums))