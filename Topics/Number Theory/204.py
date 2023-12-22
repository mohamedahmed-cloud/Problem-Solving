import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0

        mark = [0] * (n + 1)
        ans = 0
        i = 2
        while i * i <= n:
            j = i * i
            if mark[j] == 0:
                while j <= n:
                    mark[j] = 1
                    j += i
            i += 1

        for i in mark[2:-1]:
            if i == 0:
                ans += 1
        return ans

slv = Solution()
print(slv.countPrimes(11))

