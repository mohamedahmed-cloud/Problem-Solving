class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        dpth, res = 0, 0
        prv = "("
        for i in s:
            if i == "(":
                dpth += 1
            else:
                dpth -= 1
                if prv == "(":
                    res += 2 ** dpth
            prv = i
        return res
slv = Solution()
print(slv.scoreOfParentheses("(()(()))"))
