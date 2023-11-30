from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for i in s:
            if i in "({[":
                stack.append(i)

            elif stack:
                if i == ')' and stack[-1] == "(":
                    stack.pop()

                elif i == '}' and stack[-1] == "{":
                    stack.pop()
                
                elif i == "]" and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            else:
                return False

        print(stack)
        return not stack