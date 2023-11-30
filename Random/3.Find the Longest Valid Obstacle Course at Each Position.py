import bisect
class Solution:
    def solve(self,obstacles):
        n = len(obstacles)
        prepare = [float('inf')] * n
        ans = []

        for i in obstacles:
            curr = bisect.bisect_right(prepare, i)
            ans.append(curr + 1)
            prepare[curr] = i
        return (ans)



solve=Solution()
print(solve.solve([2,2,1]))