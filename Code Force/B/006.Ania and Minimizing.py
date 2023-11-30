import sys,math
n,k=map(int,sys.stdin.readline().split())
s=sys.stdin.readline().strip()
if n==k and n==1:
    print("0")
elif n==k and n>1:
    print("1"+"0"*(n-1))
elif k==0:
    print(s)
else:
    out="1"
    if s[0]!="1":
        k-=1
    for i in range(1,n):
        if s[i]!="0" and k>0:
            k-=1
            out+="0"
        else:out+=s[i]
    print(out)