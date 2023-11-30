class Solution:
    def reverseParentheses(self, s: str) -> str:
            
        curr = ""
        indx = 0

        for i in s:
            if i != ")":
                curr += i

            else:
                currcurr = ""

                for j in range(indx - 1, -1, -1):
                    if curr[j] == "(": break
                    currcurr += curr[j]

                currcurr[::-1]
                curr = curr[:j ] + currcurr

                indx -= 2
            indx += 1
            # print(curr, indx)
        return curr




    
slv = Solution()
print(slv.reverseParentheses("(((abcd)))"))

# 
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [""]
        for i in s:
            if i == '(':
                stack.append("")
            elif i == ")":
                x = stack.pop()
                stack[-1] += x[::-1]
            else:
                stack[-1] += i

        return stack[0]
                


slv = Solution()
print(slv.reverseParentheses("(ed(et(oc))el)"))