from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n = len(l)
        ans = []
        for i in range(n):
            new_arr = sorted(nums[l[i]: r[i] + 1])
            new_n = len(new_arr)
            flag = True
            prev = float("inf")
            for i in range(new_n - 1):
                if prev != float("inf") and prev != new_arr[i] - new_arr[i + 1]:
                    ans.append(False)
                    flag = False
                    break
                prev = new_arr[i] - new_arr[i + 1]
            if flag:
                ans.append(True)

        return ans


slv = Solution()
nums = [4,6,5,9,3,7]
l = [0,0,2]
r = [2,3,5]

print(slv.checkArithmeticSubarrays(nums, l, r))
