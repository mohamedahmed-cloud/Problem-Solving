import sys,math
n=int(sys.stdin.readline())
s=sys.stdin.readline().strip()
ans=""
if n %2!=0:
    for i in range(n):
        if i%2==0:
            ans+=s[i]
        else:
            ans=s[i]+ans
    print(ans)
else:
    for i in range(n):
        if i%2!=0:
            ans+=s[i]
        else:
            ans=s[i]+ans
    print(ans)