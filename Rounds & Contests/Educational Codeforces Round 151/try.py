t = int(input())

for _ in range(t):
    n, k, x = map(int, input().split())

    # Initialize list of integers from 1 to k, except for x
    nums = list(range(1, x)) + list(range(x+1, k+1))

    # Try to find a subset of nums that adds up to n
    ans = []
    for i in range(len(nums)):
        while nums[i] <= n:
            ans.append(nums[i])
            n -= nums[i]
        if n == 0:
            print("YES")
            print(len(ans), *ans)
            break

    if n != 0:
        print("NO")