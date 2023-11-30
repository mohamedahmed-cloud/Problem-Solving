def grid(n,m):
    if n==1 or m==1 : return 1
    if n==0 or m==0 : return 0
    return grid(n-1,m)+grid(n,m-1)
print(grid(2,4)) 