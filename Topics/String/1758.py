class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        def count(s, val):
            cnt0 = 0
            cnt1 = 0
            for i in range(n):
                if i & 1 == val:
                    if s[i] != "0":
                        cnt0 += 1
                    else:
                        cnt1 += 1
                else:
                    if s[i] != "1":
                        cnt0 += 1
                    else:
                        cnt1 += 1
            return min(cnt1, cnt0)
        return count(s, 0)


slv = Solution()
s = "110010"
print(slv.minOperations(s))
