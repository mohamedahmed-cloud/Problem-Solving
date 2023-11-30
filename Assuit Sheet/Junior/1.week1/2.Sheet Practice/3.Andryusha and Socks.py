def solve():
    my_set=set()
    max=0
    add=0
    for i in arr:
        if i not in my_set:
            my_set.add(i)
            add+=1
        else:
            add-=1
        if max<add:
            max=add 
    return max
import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
print(solve())