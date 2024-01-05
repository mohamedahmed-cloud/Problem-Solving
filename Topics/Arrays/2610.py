from typing import List
from collections import Counter

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        cnt = max(count.values())
        ans = []
        for i in range(cnt):
            tmp = []
            for key, value in count.items():
                if value > 0:
                    tmp.append(key)
                    count[key] -= 1
            
            ans.append(tmp)
        return ans

slv = Solution()
nums = [1,3,4,1,2,3,1]
print(slv.findMatrix(nums))
