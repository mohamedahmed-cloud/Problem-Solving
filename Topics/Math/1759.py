class Solution:
    def countHomogenous(self, s: str) -> int:
        prev = ""
        ans = 0
        s += "A"
        mod = 10**9 + 7

        for i in s:
            if not prev:
                prev = i
            elif prev[-1] == i:
                prev += i
            else:
                # print(prev)
                n = len(prev)
                ans += (n * (n + 1)) // 2
                prev = i
        
        return ans % mod
slv = Solution()
print(slv.countHomogenous( "zzzzz"))