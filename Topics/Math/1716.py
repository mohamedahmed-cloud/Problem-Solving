class Solution:
    def totalMoney(self, n: int) -> int:
        curr = 7 * 8 // 2
        ans = 0
        start = 0

        while n >= 7:
            n -= 7
            ans += curr
            curr += 7
            start += 1

        # print(ans, start)
        while n != 0:
            start += 1
            ans += start
            n -= 1
        return ans

slv = Solution()
n = 20
print(slv.totalMoney(n))