def Sum_Of_Natural_Number(n,ans):
    if n==0:
        return ans
    ans+=n
    return Sum_Of_Natural_Number(n-1,ans)
import sys,math
n=int(sys.stdin.readline())
ans=0
print(Sum_Of_Natural_Number(n,ans))