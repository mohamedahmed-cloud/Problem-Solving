import sys,math,bisect
n,m=map(int, sys.stdin.readline().split())
arr=list(set(map(int,sys.stdin.readline().split())))
arr.sort()
n=len(arr)
for i in range(m):
    s,key=map(str,sys.stdin.readline().split())
    if s=="binary_search":
        a=bisect.bisect_left(arr,int(key))
        if a<n:
            if arr[a]==int(key):
                print("found")
            else:
                print("not found")
        else:print("not found")
    elif s=="lower_bound":
        a=bisect.bisect_left(arr,int(key))
        if a<n:
            if arr[a]>=int(key):
                print(arr[a])
            else:
                print(-1)
        else:print(-1)
    elif s=="upper_bound":
        a=bisect.bisect(arr,int(key))
        if a<n:
            if arr[a]>int(key):
                print(arr[a])
            else:
                print(-1)
        else:print(-1)
                

