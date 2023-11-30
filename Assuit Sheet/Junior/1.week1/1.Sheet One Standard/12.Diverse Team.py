import sys,math
# def solve():
    
n,k=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
my_list=list(set(arr))
a=len(my_list)
if a>=k:
    print("YES")    
    for i in range(k):
        print(arr.index(my_list[i])+1,end=' ')
else:
    print("NO")

