
from collections import defaultdict
from typing import Optional, List
from heapq import heappush, heappop, heapify
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = defaultdict(int)
        for i in words:
            freq[i] += 1
        heap = []
        
        for key, value in freq.items():
            heap.append((-value, key))
        heapify(heap)
        print(heap)
        ans = []
        for i in range(k):
            ans.append(heappop(heap)[1])
        return ans
slv = Solution()
words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
k = 2
print(slv.topKFrequent(words, k))

