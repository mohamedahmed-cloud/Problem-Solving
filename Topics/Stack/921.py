from collections import deque

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = deque()
        n = 0
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
                    n +=1 
            else:
                n += 1

        return len(stack) + n