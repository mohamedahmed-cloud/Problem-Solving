class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for i in s:
            if i == "(":
                stack.append(i)
            else:
                if stack[-1] == "(":
                    stack.pop()
                    stack.append(1)
                else:
                    ans = 0
                    while stack[-1] != "(":
                        ans += stack.pop()
                    stack.pop()
                    stack.append(2 * ans)
            print(stack)

        return sum(stack)


slv = Solution()
print(slv.scoreOfParentheses("(())(())"))

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        curr = 0
        for i in s:
            if i == "(":
                stack.append(curr)
                curr = 0
            else:
                curr = max(2 * curr , 1) + stack.pop()
        return curr