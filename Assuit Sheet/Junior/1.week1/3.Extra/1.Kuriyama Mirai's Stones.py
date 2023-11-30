import sys,math

n=int(sys.stdin.readline())
cost=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
#######
# Storing
# cost.insert(0,0)
# print(cost)
ans1=cost.copy()
ans1.insert(0,0)
ans2=cost.copy()
ans2.sort()
ans2.insert(0,0)
# answer one
# print(ans2)
# print(ans1,ans2)
for i in range(1,n+1):
    ans1[i]+=ans1[i-1]
    ans2[i]+=ans2[i-1]
# print(ans1,ans2)

for i in range(m):
    q,l,r=map(int,sys.stdin.readline().split())
    if q==1:
        print(ans1[r]-ans1[l-1])
    elif q==2:
        print(ans2[r]-ans2[l-1])