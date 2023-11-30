class Solution:
    def sortVowels(self, s: str) -> str:
        t = ""
        vowels = { "A":0,   "E":0,  "I":0,  "O":0,   "U":0,
                    'a':0,  'e':0,   'i':0,  'o':0,   'u':0}

        for i in s:
            if i in vowels:
                vowels[i] += 1
    
        for i in s:
            if i in vowels:
                for key, value in vowels.items():
                    if value != 0:
                        t += key
                        vowels[key] -= 1
                        break
            else:
                t += i
        return t

slv = Solution()
print(slv.sortVowels("lYmpH"))

