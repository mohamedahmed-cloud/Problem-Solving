def solve(a,b):
    ans=0
    while True:
        if a==1 or b==1 :
            ans+=max(a,b)
            break
        if a==0 or b==0:
            break
        w=a
        z=b
        ans+=w//z   
        b=w%z 
        a=z
        # print(a,b,ans)
    return ans
import sys
a,b=map(int, sys.stdin.readline().split())
ans=solve(a,b)
print(ans)