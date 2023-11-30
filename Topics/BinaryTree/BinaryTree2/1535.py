from typing import Optional, List
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        stack = []
        n = len(arr)
        if k >= n:
            return max(arr)
        if k == 1:return max(arr[0], arr[1])

        max_element = max(arr[0], arr[1])
        curr_k = 0

        for i in range(1, n):
            if arr[i] >= max_element:
                max_element = arr[i]
                curr_k = 1
            else:
                curr_k += 1
            if curr_k == k :
                return max_element
        return max(arr)

slv = Solution()
arr = [1,25,35,42,68,70]
k = 2
print(slv.getWinner(arr, k))