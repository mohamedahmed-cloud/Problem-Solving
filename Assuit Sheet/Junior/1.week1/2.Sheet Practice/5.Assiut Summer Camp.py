import sys,math
def solve():
    a=max(arr)
    first=my_list[arr.index(a)]
    b=0
    for i in arr:
        if b<i and i!=a:
            b=i
    second=my_list[arr.index(b)]
    print(first, second)
    
n=int(sys.stdin.readline())
my_list=["Hussien","Atef","Karemo","Ezzat"]
for i in range(n):
    arr=list(map(int,sys.stdin.readline().split()))
    solve()