from typing import Optional, List

class Solution:
    def minOperations(self, logs: List[str]) -> int:

        check = ["../", "./"]
        d = 0
        for i in logs:
            if i == check[0]:
                d -= 1
                d = max(d, 0)
                
            elif i == check[1]:
                continue
            else:
                d += 1
        return d