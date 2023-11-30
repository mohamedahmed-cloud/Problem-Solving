from typing import Optional, List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        freq = [0] * (len(nums) + 1)

        for i in nums:
            if freq[i]:
                return i
            freq[i] += 1
            

# tricky solution.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for i,val in enumerate(nums):
            nums[abs(val)] *= -1
            if nums[abs(val)] > 0: 
                return abs(val)
