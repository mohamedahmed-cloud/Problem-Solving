from typing import List
from functools import reduce
from collections import Counter
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums = Counter(nums)
        # print(nums)
        nums = sorted(nums.items(), key=lambda x: x[0])
        cnt = 0
        ans = 0
        for i in nums:
            ans += cnt * i[1]
            cnt += 1
        # print(ans)
        return ans
slv = Solution()
nums = [5, 1,2,2,3]
print(slv.reductionOperations(nums))

        