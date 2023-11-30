def solve(n,s,ans):
    if n==0:
        return ans
    if s[n-1] in ['a','A', 'e',"E", 'i',"I", 'o',"O", 'u',"U"]:
        ans+=1
    return solve(n-1,s,ans)
import sys,math
s=sys.stdin.readline()
s=s[:-1]
n=len(s)
ans=0
print(solve(n,s,ans))