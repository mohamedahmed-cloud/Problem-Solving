from typing import List
from collections import defaultdict, Counter
import math

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        for i in nums:
            cnt[i] += 1
        print(cnt)
        res = 0
        for key, value in cnt.items():
            while value:
                if value > 4:
                    value -= 3
                elif value == 3:
                    value = 0
                elif value == 1:
                    return -1
                else:
                    value -= 2
                res += 1
        return res 


slv = Solution()
nums = [2,3,3,2,2,4,2,3,4, 2, 2, 2]
print(slv.minOperations(nums))

# another solution 
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        # print(cnt)
        res = 0
        for value in cnt.values():
            if value == 1: return -1
            elif value % 3 == 0: res += value // 3
            else: res += value // 3 + 1
        return res

slv = Solution()
nums = [2,3,3,2,2,4,2,3,4, 2, 2, 2]
# nums = [2,1,2,2,3,3]
print(slv.minOperations(nums))


# another solution 
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        # print(cnt)
        res = 0
        for value in cnt.values():
            if value == 1: return -1
            res += math.ceil(value / 3)
        return res

slv = Solution()
nums = [2,3,3,2,2,4,2,3,4, 2, 2, 2]
# nums = [2,1,2,2,3,3]
print(slv.minOperations(nums))