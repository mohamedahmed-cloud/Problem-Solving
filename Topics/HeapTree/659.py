#!/usr/bin/env python3
from collections import Counter
from typing import Optional, List

class Solution:
	def isPossible(self, nums: List[int]) -> bool:
		counter = Counter(nums)
		sorted_array = sorted(counter.keys())

		for i in sorted_array:
			while counter[i] > 0:
				prev = 0
				j = i
				cnt = 0
				while counter[j] >= prev:
					# print(counter)
					prev = counter[j]
					counter[j] -= 1
					cnt += 1
					j += 1
				if cnt < 3:
					return False
		return True


slv = Solution()
nums = [1,2,3,4,4,5,5]
print(slv.isPossible(nums))