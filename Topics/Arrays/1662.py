from typing import List
from functools import reduce
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 = reduce(lambda x,y : x + y, word1)
        s2 = reduce(lambda x,y: x + y, word2)
        return s1 == s2


slv = Solution()
word1 = ["ab", "c"]
word2 = ["a", "bc"]
print(slv.arrayStringsAreEqual(word1, word2))
