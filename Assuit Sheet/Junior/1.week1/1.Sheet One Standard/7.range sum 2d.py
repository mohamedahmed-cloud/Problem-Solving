# Runtime error on test two
def solve(arr):
    for i in range(1,n+1):
        for j in range(1,m+1):
            arr[i][j]+=arr[i][j-1]
    for i in range(1,m+1):
        for j in range(1,n+1):
            arr[j][i]+=arr[j-1][i]
import sys,math
n,m,q=map(int,sys.stdin.readline().split())
arr=[]
add=[]
# make arr one indexing

for i in range(m):
    add.append(0)
arr.append(add)
for i in range(n):
    # take an 2D array from user
    arr.append(list(map(int,sys.stdin.readline().split())))
    # make arr one indexing
    arr[i].insert(0,0)
arr[-1].insert(0,0)
solve(arr)
for i in range(q):
    x1,y1,x2,y2=map(int,sys.stdin.readline().split())
    a=(arr[x2][y2]+arr[x1-1][y1-1])-(arr[x2][y1-1]+arr[x1-1][y2])
    print(a)