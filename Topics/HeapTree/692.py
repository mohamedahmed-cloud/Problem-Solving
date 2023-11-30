#!/usr/bin/env python3

from collections import defaultdict
from typing import Optional, List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = defaultdict(int)
        for i in words:
            freq[i] += 1
        freq = sorted(freq.items(), key = lambda x: (-x[1], x[0]))
        print(freq)
        return [key for key, value in freq[:k]]
slv = Solution()
words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
k = 4
print(slv.topKFrequent(words, k))

