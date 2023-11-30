def sum(n,l,ans,store):
    if n==0:
        return (ans/store)
    ans+=l[n-1]
    return sum(n-1,l,ans,store)



import sys,math
n=int(sys.stdin.readline())
l=list(map(int,sys.stdin.readline().split()))
store=n
ans=0
a=sum(n,l,ans,store)
print(f"{a:.6f}")
