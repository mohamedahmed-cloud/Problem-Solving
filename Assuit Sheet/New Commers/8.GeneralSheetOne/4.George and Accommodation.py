import sys
count=0
rooms=int(input())
for i in range(rooms):
    n,k=map(int,sys.stdin.readline().split())
    if k-n>=2:
        count+=1
print(count)