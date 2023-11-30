from typing import Optional, List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        ans = set()
        def find(i):
            if  i >= len(arr) or i < 0: return False
            if arr[i] == 0: return True
            if (arr[i], i) in ans: return False
            ans.add((arr[i],i))
            return find(i - arr[i]) or find(i + arr[i])

        return find(start)