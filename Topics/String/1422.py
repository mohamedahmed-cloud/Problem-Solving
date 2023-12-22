class Solution:
    def maxScore(self, s: str) -> int:
        ones = 0
        for i in s[1:]:
            if i == "1":
                ones += 1
        zeros = 1 if s[0] == "0" else 0
        ans = ones + zeros 
        for i in s[1:-1]:
            if i == "1":
                ones -= 1
            elif i == "0":
                zeros += 1
            if ones + zeros > ans:
                ans = ones + zeros
        return ans

slv = Solution()
s = "00"
print(slv.maxScore(s))