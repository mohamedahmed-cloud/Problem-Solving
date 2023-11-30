def Print_Recursion(n,ans=""):
    if n==0:
        return ans
    if n==1:
        ans+="I love Recursion"
    else:
        ans+="I love Recursion"+"\n"
    return Print_Recursion(n-1,ans)
import sys,math
n=int(sys.stdin.readline())
ans=""
print(Print_Recursion(n,ans))