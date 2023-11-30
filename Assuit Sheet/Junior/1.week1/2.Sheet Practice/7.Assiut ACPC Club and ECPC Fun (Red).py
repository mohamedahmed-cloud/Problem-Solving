# Time limit in test 8
import sys,math
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
q=int(sys.stdin.readline())
for i in range(q):
    l,r=map(int,sys.stdin.readline().split())
    arr=arr[:l-1]+[0]*(r-l+1)+arr[r:]
s=""
count=0
for i in arr:
    if i!=0:
        count+=1
        s+=str(i)+" "
sys.stdout.write(str(count) + "\n")
sys.stdout.write(s)

