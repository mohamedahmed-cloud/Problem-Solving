from collections import defaultdict
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        dict = defaultdict(list)

        # {"x": [start, end] }
        # answer is += len(set(s[start +1 : end])

        for i, value in enumerate(s):
            if value in dict:
                dict[value] = [dict[value][0], i]
            else:
                dict[value] = [i, i]
        ans = 0
        for key, value in dict.items():
            start, end = value
            x = set(s[start + 1 : end])
            ans += (len(x))

        return ans

slv = Solution()
s = "tlpjzdmtwderpkpmgoyrcxttiheassztncqvnfjeyxxp"
print(slv.countPalindromicSubsequence(s))