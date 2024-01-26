class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        n = len(s)
        i = 0

        while i < n - 1:
            if s[i] == s[i + 1]:
                if i + 2 < n:
                    s = s[: i] + s[i + 2: ]
                else:
                    s = s[: i]

                if i > 0:
                    i -= 1
            else:
                i += 1

            n = len(s)

        return s



# Using stack.
class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack = []
        
        for i in s:
            if stack and  i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
            
        return "".join(stack)
        