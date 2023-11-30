# Time Limit In test 2
import sys,math
def solve(freq):
    for i in arr:
        freq[i] +=1
n,q=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
arr=list(set(arr))
l=len(arr)
freq=[0]*(10**5+1)
solve(freq)
for i in range(q):
    a=int(sys.stdin.readline())
    b=freq[:a].count(1)
    if freq[l-b]==1:
        print(b,l-b-1)
    else:print(b,l-b)