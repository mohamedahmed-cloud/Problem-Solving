def solve(n):
    if n==0:return 0
    return n+solve(n-1)
print(solve(int(input())))