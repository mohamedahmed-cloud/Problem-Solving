class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # ( (high+1) // 2)
        return ( (high+1) // 2)-(low//2)