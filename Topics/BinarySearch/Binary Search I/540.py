from typing import Optional, List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        n = 0
        for i in nums:
            n ^= i
        return n

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            if mid % 2: mid -= 1
            if nums[mid] == nums[mid + 1]:
                l = mid + 2
            else: 
                r = mid

        return nums[l]

                