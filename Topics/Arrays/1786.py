class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        n1 = len(word1)
        n2 = len(word2)
        for i, j in zip(word1, word2):
            ans += i + j
        if n1 > n2:
            ans += word1[n2:]
        else:
            ans += word2[n1:]
        return ans

