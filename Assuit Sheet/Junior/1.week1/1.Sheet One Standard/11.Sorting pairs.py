import math,sys
n=int(sys.stdin.readline())
arr=[]
for i in range(n):
    arr.append(list(map(str,sys.stdin.readline().split())))
arr.sort()
ans=sorted(arr,key=lambda x:int(x[1]) ,reverse=True)
for i in ans:
    print(*i)