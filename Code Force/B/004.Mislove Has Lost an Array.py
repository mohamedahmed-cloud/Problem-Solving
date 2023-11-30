import sys,math
n,x,y=map(int,sys.stdin.readline().split())
ans1=0
ans2=0
ans1+=n-(x-1)
start=2
for i in range(x-1):
    ans1+=start
    start*=2

diff=y
start=1
for i in range(n):
    ans2+=start
    diff-=1
    if diff>0:
        start*=2
print(ans1,ans2)