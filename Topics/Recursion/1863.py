# Recursion using memoziation.

from typing import List
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        n = len(nums)
        def xor(val, i, memo = {}):
            nonlocal n

            if i == n:
                return val
                
            if (val, i) in memo:
                return memo[(val, i)]
            
            memo[(val, i)] = xor(val ^ nums[i], i + 1, memo) + xor(val, i + 1, memo)
            return memo[(val, i)]
        
        return xor(0, 0)
