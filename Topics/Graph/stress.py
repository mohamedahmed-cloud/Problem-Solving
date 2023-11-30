for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(range(1, n + 1))
    for i in range(n + 1):
        if i == n or a[n-i-1] == 0:
            break
    b.insert(n-i, n+1)
    print(*b)
