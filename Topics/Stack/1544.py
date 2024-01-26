class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        def check(i):
            if stack:
                return stack[-1] == s[i].lower() and s[i] != s[i ].lower() or \
                stack[-1] == s[i].upper() and s[i] != s[i].upper()

            return False
        for i in range(len(s)):
            if not check(i):
                stack.append(s[i])
            elif stack:
                stack.pop()
    

        return "".join(stack)
                
