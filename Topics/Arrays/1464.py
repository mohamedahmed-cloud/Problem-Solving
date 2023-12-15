from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx = max(nums)
        mx_index = nums.index(mx)
        mx = (mx, mx_index)
        # print(mx)
        mx_2 = (-float("inf"), 0)
        for i, val in enumerate(nums):
            if val > mx_2[0] and i != mx[1]:
                mx_2 = (val, i)
        # print(mx, mx_2)
        return (mx_2[0] -1 ) * (mx[0] - 1)

slv = Solution()
nums = [1, 5, 4, 5]
print(slv.maxProduct(nums))
