from typing import List
from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        arr = [0] * 26
        for i in chars:
            arr[ord("a") - ord(i)] += 1
        ans = 0
        for i in words:
            x = Counter(i)
            flag = True
            for key, val in x.items():
                if val > arr[ord("a") - ord(key)]:
                    flag = False
                    break
            if flag:
                # print(i)
                ans += len(i)
                # for key, val in x.items():
                #     arr[ord("a") - ord(key)] -= val
        return ans




slv = Solution()
words = ["hello","world","leetcode"]
chars = "welldonehoneyr"
print(slv.countCharacters(words, chars))
