def solve(A,B,R,C,ans):
    if R==0:
        return ans
    for j in range(C):
        ans[R-1][j]=A[R-1][j]+B[R-1][j]
    return solve(A,B,R-1,C,ans)
import sys,math
A=[]
B=[]
R,C= map(int, sys.stdin.readline().split())
ans=[[int(0) for x in range(C)]for j in range(R)]
# print(ans)
for i in range(R):
    A.append(list(map(int,sys.stdin.readline().split())))

for i in range(R):
    B.append(list(map(int,sys.stdin.readline().split())))
# print(A,B)
out=solve(A,B,R,C,ans)
for i in out:
    print(*i)