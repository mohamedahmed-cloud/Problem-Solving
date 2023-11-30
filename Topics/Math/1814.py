from typing import List
from collections import defaultdict
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        n = len(nums)
        new_nums = []
        for i in nums:
            new_nums.append(i - int(str(i)[::-1]))

        count = defaultdict(int)
        for i in new_nums:
            count[i] += 1
        ans = 0
        for key, value in count.items():
            if value >= 1:
                ans += (value) * (value - 1) // 2
        return ans % (10**9 + 7)
slv = Solution()
nums = [42,11,1,97]
print(slv.countNicePairs(nums))
