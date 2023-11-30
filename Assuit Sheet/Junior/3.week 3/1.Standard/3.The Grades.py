# not solved yet
import sys,math,bisect
t=int(sys.stdin.readline())
all=[]
for i in range(t):
    arr=list(map(str,sys.stdin.readline().split()))
    add=int(arr[1])+int(arr[2])+int(arr[3])+int(arr[4])
    arr.insert(1,add)
    bisect.insort(all,arr)
    
# all.sort(key=lambda x:x[1],reverse=True)
for i in all:
    print(i)