class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        l = 0 # (
        r = 0 # )
        # ())()(((

        for i in s:
            if i == "(":
                stack.append("(")
                l += 1
            elif i == ")":
                if l > r:
                    stack.append(")")
                    r += 1
            else:
                stack.append(i)
        
        if l == r: return "".join(stack)
        # take many left.
        else:
            # print("here")
            n = len(stack)
            # print(n)
            # print(stack)
            l = 0
            r = 0
            ans = ""

            for i in range(n-1, -1, -1):
                if stack[i] == "(":
                    if l < r:
                        ans += "("
                        l += 1

                elif stack[i] == ")":
                    ans += ")"
                    r += 1

                else:
                    ans += stack[i]
                # print(ans, i)

            return ans[::-1]

                





slv = Solution()
print(slv.minRemoveToMakeValid("())()(((")) 