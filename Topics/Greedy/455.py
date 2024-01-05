from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        gn, sn = len(g), len(s)
        gi = si = 0
        ans = 0
        g.sort()
        s.sort()

        while gi < gn and si < sn:
            if s[si] >= g[gi]:
                ans += 1
                gi += 1
            si += 1
        return ans
