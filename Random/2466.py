class Solution:
    def solve(self, low, high, zero, one):
        dp = [0] * (high + 1)
        dp[0] = 1

        for i in range(min(zero,one), high + 1):
            if i >= zero:
                dp[i] += dp[i - zero]
            if i >= one:
                dp[i] += dp[i - one]
        print(dp)
        return sum(dp[low:high + 1])
    

solve=Solution()
print(solve.solve(4, 4, 1, 4))