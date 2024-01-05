from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        ans = 0
        for i in bank:
            curr = i.count("1")
            ans += prev * curr
            if curr:
                prev = curr
        return ans

slv = Solution()
bank = ["011001","000000","010100","001000"]
print(slv.numberOfBeams(bank))
