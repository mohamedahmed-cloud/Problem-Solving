from itertools import groupby
class Solution:
    def solve(chars):
        ans=""
        n=len(chars)
        iter=1
        i=0
        for i in range(1,n):
            if chars[i]==chars[i-1]:
                iter+=1
            else:
                if iter>1:
                    ans+=(chars[i-1]+str(iter))
                else:
                    ans+=chars[i-1]
                iter=1
        if iter>1:
            ans+=(chars[i-1]+str(iter))
        else:
            ans+=chars[i]
        x=list(ans)
        for i in range(len(x)):
            chars[i]=x[i]
        print(chars)
        return len(ans)
solve=Solution
print(solve.solve(["a","b","c"]))


          