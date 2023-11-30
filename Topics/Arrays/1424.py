from typing import List
from collections import deque, defaultdict
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        i, j = -1, -1
        ans = defaultdict(list)
        for row in nums:
            i += 1
            j = -1
            for col in row:
                j += 1
                ans[i + j].append(col)
        res = []
        for key, value in ans.items():
            value = value[::-1]
            res.extend(value)

        return ans
slv = Solution()
nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
slv.findDiagonalOrder(nums)
