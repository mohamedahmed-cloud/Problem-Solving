class Solution:
    def solve(self, path):
        temp = path.split("/")
        ans = ["/"]
        for i in temp:
            if i in ["", "."]:
                continue
            if i in [".."]:
                if len(ans) > 2:
                    ans = ans[:-2]
                continue
            ans.append(i)
            ans.append("/")
        if ans[:-1]:
            return "".join(ans[:-1])
        return "".join(ans)
solve=Solution()
print(solve.solve( "/./"))