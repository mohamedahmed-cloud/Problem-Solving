from typing import List

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        curr = [float("inf"), 1]
        mx = [arr[0], 0]
        for i in range(1, n):
            if arr[i - 1] == arr[i]:
                curr[1] += 1
            else:
                curr[1] = 1
            curr[0] = arr[i]

            if mx[1] < curr[1]:
                mx = curr[:]
        return mx[0]