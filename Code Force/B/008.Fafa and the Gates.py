import sys,math
n=int(sys.stdin.readline())
s=sys.stdin.readline().strip()
ans=0
move=0
arr=[0]*n
iter=0
for i in s:
    if i=="U":
        move-=1
        arr[iter]=move
        if iter>=2 and arr[iter-1]==0 and arr[iter-2]>0:
            ans+=1 
    else:
        move+=1
        arr[iter]=move
        if iter>=2 and arr[iter-1]==0 and arr[iter-2]<0:
            ans+=1
    iter+=1
print(ans)
