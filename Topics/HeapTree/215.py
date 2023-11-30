from typing import Optional, List
from heapq import heapify, heappop, heappush

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums = [-i for i in nums]
        # heapify(nums)
        # print(nums)
        # while k > 1:
        #     heappop(nums)
        #     k -= 1
        # return -heappop(nums)
        ans = []
        heapify(ans)
        n = 0

        for i in nums:
            if n < k:
                heappush(ans, i)
                n += 1

            elif i > ans[0]:
                heappop(ans)
                heappush(ans, i)

        return ans[0]

slv = Solution()
nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(slv.findKthLargest(nums, k))

