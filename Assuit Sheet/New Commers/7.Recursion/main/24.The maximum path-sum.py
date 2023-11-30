import sys
def solve(start,end):
    if start==n-1 and end==c-1:
        return arr[n-1][c-1]
    elif start==n or end==c:
        return -10e7
    right=solve(start+1,end)
    down=solve(start,end+1)
    return arr[start][end]+max(right,down)
    

n,c=tuple(map(int, sys.stdin.readline().split()))
# n,c=map(int, sys.stdin.readline().split())
arr=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
# print(arr)
start=0
end=0
print(solve(start,end))