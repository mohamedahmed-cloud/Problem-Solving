from collections import Counter, defaultdict
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        l1 = [0] * 26
        l2 = [0] * 26
        n1 = len(word1)
        n2 = len(word2)

        for i in range(n1):
            l1[ord("a") - ord(word1[i])] += 1
            l2[ord("a") - ord(word2[i])] += 1

        return n1 == n2 and sorted(l1) == sorted(l2) and set(word1) == set(word2)

word1 = "ab"
word2 = "aa"
slv = Solution()
print(slv.closeStrings(word1, word2))

# another solution
from collections import Counter, defaultdict
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        l1 = Counter(word1)
        l2 = Counter(word2)
        test = l1.keys() == l2.keys()
        for key, val in l1.items():
            flag = True
            for k2, val2 in l2.items():
                if val == val2 and test:
                    flag = False
                    l2[k2] = "0"
                    break
            if flag: return False 

        return True
word1 = "cca"
word2 = "aac"
slv = Solution()
print(slv.closeStrings(word1, word2))
