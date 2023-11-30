from collections import defaultdict
class Solution:
    def solve(self, rectangles):
        l = defaultdict(int)
        ans = 0
        for i in rectangles:
            l[i[1]/i[0]] += 1
        for i in l.values():
            ans += (i - 1) * i//2
        return ans
    
solve=Solution()
print(solve.solve([[4,5],[7,8]]))