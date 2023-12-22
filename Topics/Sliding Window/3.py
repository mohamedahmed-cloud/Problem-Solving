from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        p1 = 0
        mx = 0
        count = defaultdict(int)
        for i in range(n):
            while p1 < n and count[s[i]] == 1:
                count[s[p1]] = 0
                p1 += 1
            if mx < i  - p1: mx = i - p1
            count[s[i]] = 1
        return mx + 1



