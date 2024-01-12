class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 2)
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 2] + dp[i - 1]
        return dp[n - 1]

slv = Solution()
n = 6
print(slv.climbStairs(n))

# another solution
class Solution:
    def climbStairs(self, n: int) -> int:
        a = 0
        b = 1

        for i in range(n):
            a, b = b, a + b
        return b

slv = Solution()
n = 6
print(slv.climbStairs(n))