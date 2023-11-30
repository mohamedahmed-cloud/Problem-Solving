import sys
n,m=map(int,sys.stdin.readline().split())
count=0
for i in range(n):
    if i%2==0:
        count+=1
        print("#"*m)
    else:
        if count%2==0:
            print("#"+"."*(m-1))
            
        else:print("."*(m-1)+"#")

