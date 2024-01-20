from collections import defaultdict

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt = {chr(97 +i): [0, 0] for i in range(26)}

        for i, j in zip(s, t):
            cnt[i][0] += 1
            cnt[j][1] += 1

        ans = 0
        for i in cnt.values():
            ans += abs(i[0] - i[1])
        return ans // 2

slv = Solution()
s = "anagram"
t = "mangaar"
print(slv.minSteps(s, t))
