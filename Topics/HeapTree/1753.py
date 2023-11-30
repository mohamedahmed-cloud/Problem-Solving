from heapq import heapify, heappop
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        l = [a, b, c]
        heapify(l)
        min_a = heappop(l)
        min_b = heappop(l)
        max_a = heappop(l)
        if max_a <= min_a + min_b:
            print((min_a + max_a + min_b) // 2)
        else:
            print(min_a + min_b)
