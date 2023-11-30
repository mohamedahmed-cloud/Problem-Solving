import sys,math,bisect,itertools
n=int(sys.stdin.readline())
s=sys.stdin.readline().strip()
arr=[]
ans=0
for i in range(2,n+1):
    arr.append(s[i-2:i])
for i in arr:
    a=arr.count(i)
    if a>ans:
        out=i
        ans=a
print(out)