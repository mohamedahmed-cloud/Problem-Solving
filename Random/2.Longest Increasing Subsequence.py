import bisect
class Solution:
    def solve(self, nums):
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        print(dp)
        return (max(dp))


solve=Solution()
print(solve.solve([0,1,0,3,2,3]))


# another solution with nlog(n)

class Solution:
    def solve(self,nums):
        ans = [nums[0]]
        n = len(nums)

        for i in range(n):
            # print(ans)
            if nums[i] > ans[-1]:
                ans.append(nums[i])
            else:
                place = bisect.bisect_left(ans, nums[i])
                if place == n:
                    ans.append(nums[i])
                else:
                    ans[place] = nums[i]
        return len(ans)     



solve=Solution()
print(solve.solve([10,9,2,5,3,7,101,18]))