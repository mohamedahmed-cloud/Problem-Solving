def solve(s):
    n=len(s)
    if s=="":
        return ""
    else:
        return solve(s[1:])+s[0]
import sys,math
s=sys.stdin.readline()
s=s[:-1]
print(solve(s))