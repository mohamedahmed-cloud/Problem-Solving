
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        n = len(s)
        half = n // 2
        a = s[: half]
        b = s[half: ]
        aa = bb = 0
        for i in a:
            if i in vowels:
                aa += 1
        for i in b:
            if i in vowels:
                bb += 1
        return aa == bb

slv = Solution()
s =  "book"
print(slv.halvesAreAlike(s))