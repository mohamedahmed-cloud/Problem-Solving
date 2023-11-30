def BaseConverssion(n,ans):
    if n==0:
        return ans[::-1]
    ans+=str(n%2)
    return BaseConverssion(n//2,ans)

import sys
t=int(sys.stdin.readline())
for i in range(t):
    n=int(sys.stdin.readline())
    ans=""
    print(BaseConverssion(n,ans))