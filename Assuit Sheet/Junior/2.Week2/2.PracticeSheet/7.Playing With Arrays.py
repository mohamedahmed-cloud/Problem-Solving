import sys,math,bisect,itertools,heapq
t=int(sys.stdin.readline())
for _ in range(t):
    n=int(sys.stdin.readline())
    arr=[x+1 for x in range(n)]
    result=[0]*n
    count1=0
    count2=0
    for i in range(n):
        if i%2==0:
            count1+=1
            result[i]=arr[i-count2]
        else:
            count2+=1
            result[i]=arr[-(i+1-count1)]
    print(*result)