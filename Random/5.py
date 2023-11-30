class Solution:
    def solve(self,s):
        n = len(s)
        ans = ""

        def func(s,i,j, n):
            while i >= 0 and j < n and s[i] == s[j] :
                i -= 1
                j += 1
            return s[i + 1 : j]

        for i in range(n):
            ans = max(ans, func(s, i, i, n), func(s, i, i + 1, n), key=len)
        return ans


solve=Solution()
print(solve.solve("cbbd"))
