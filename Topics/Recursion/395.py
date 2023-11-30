import collections

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        def find(s):
            count = collections.Counter(s)
            # print(count)
            for i, value in enumerate(s):
                if count[value] < k:
                    return max(find(s[:i]), find(s[i + 1 :]))
            
            return len(s)
        return find(s)


slv = Solution()
print(slv.longestSubstring("aaabb", 3))