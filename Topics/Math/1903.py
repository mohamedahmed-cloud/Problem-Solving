class Solution:
    def largestOddNumber(self, num: str) -> str:
        last = 0
        odd = set("13579")
        n = len(num)
        for i in range(n - 1, -1, -1):
            if num[i] in odd:
                return num[:i + 1]

slv = Solution()
num = "354267"
print(slv.largestOddNumber(num))