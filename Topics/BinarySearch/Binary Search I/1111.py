from typing import Optional, List
from collections import deque

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:

        res = deque()
        cnt = 0

        for i in seq:
            if i == "(":
                cnt += 1

            res.append(cnt % 2)
            if i == ")":
                cnt -= 1
        return res