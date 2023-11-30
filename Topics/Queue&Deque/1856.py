from typing import List

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        stack = []
        res = 0


        for i in range(n + 1):
            while stack and (i == n or nums[stack[-1]] > nums[i]):
                curr = stack.pop()
                ans = (prefix_sum[i] - prefix_sum[stack[-1] + 1 if stack else 0]) * nums[curr]
                # print(prefix_sum[i], prefix_sum[curr], i, curr, "ans", ans)
                if ans > res:
                    # print("role", nums[curr], ans)
                    res = ans 
                # print(ans, curr)
            stack.append(i)
            # print(stack)
        # print(stack)
        return res

slv = Solution()
nums = [1,1,3,2,2,2,1,5,1,5]
print(slv.maxSumMinProduct(nums))

