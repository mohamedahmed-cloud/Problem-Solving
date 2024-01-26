class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        n = len(s)
        i = 0
        prev = ans = ""
        ans = []

        while i < n:
            if s[i] == "(" and prev == s[i]:
                d = 0
                prev = s[i]
                while d >= 0 and i < n:
                    if s[i] == "(":
                        d += 1
                        ans.append(s[i])
                    elif d != 0:
                        d -= 1
                        ans.append(s[i])
                    else:d -= 1
                
                    prev = s[i]
                    i += 1

                    
            else:
                prev = s[i]
                i += 1


        return "".join(ans)
