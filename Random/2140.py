class Solution:
    def solve(self, questions):
        n = len(questions)
        dp = [-1] * (n + 1)
        print(dp)
        for i in range(n - 1, -1 , -1):
            compare = questions[i][0]

            if i + questions[i][1] + 1 < n:
                compare += dp[i + questions[i][1] + 1]

            if compare > dp[i + 1]:
                dp[i] = compare

            else:
                dp[i] = dp[i + 1]

        print(dp)
        return max(dp)





solve=Solution()
print(solve.solve([[3,2],[4,3],[4,4],[2,5]]))
