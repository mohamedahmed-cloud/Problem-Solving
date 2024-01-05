class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        self.s1 = s1
        self.s2 = s2

        self.l = [len(s1),  len(s2)]
        return self.LCS(0, 0, {})

    def LCS(self, i, j, memo):
        if (i >= self.l[0] or j >= self.l[1]):
            return 0

        if (i, j) in memo:
            return memo[(i, j)]


        if self.s1[i] == self.s2[j]:
            memo[(i, j)] = 1 + self.LCS(i + 1, j + 1, memo)
            return memo[(i, j)]

        else:
            memo[(i, j)] = max(self.LCS(i + 1, j, memo), self.LCS(i, j + 1, memo))
            return memo[(i, j)]

slv = Solution()
text1 = "bsbininm"
text2 = "jmjkbkjkv"
print(slv.longestCommonSubsequence(text1, text2))

# another solution
class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        return self.DP(s1, s2)
        
    def DP(self, s1, s2):
        n1 = len(s1)
        n2 = len(s2)
        res = [[0] * (n2 + 1) for i in range(n1 + 1)]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    # print("yes")
                    res[i][j] = 1 + res[i - 1][j - 1]
                else:
                    res[i][j] = max(res[i][j - 1], res[i - 1][j])


        return res[n1][n2]


slv = Solution()
text1 = "abcba"
text2 = "abcbcba"
print(slv.longestCommonSubsequence(text1, text2))

