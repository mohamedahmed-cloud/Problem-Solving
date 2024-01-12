class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0] * (n + 3)
        dp[0] = 0
        dp[1] = dp[2] = 1
        track = 2

        for i in range(3, n + 1):
            dp[i] = track
            track += dp[i] - dp[i - 3]
        return dp[n]
