def max_experience(t, test_cases):
    for test_case in test_cases:
        n, k = test_case[0], test_case[1]
        a_values = test_case[2]
        b_values = test_case[3]

        max_experience = 0
        max_experience_list = []

        for i in range(n - 1, -1, -1):
            max_experience += a_values[i]
            if i < n - 1:
                max_experience += (k - 1) * b_values[i]

            max_experience_list.append(max_experience)

        print(max(max_experience_list))

# Input reading
t = int(input())
test_cases = []

for _ in range(t):
    n, k = map(int, input().split())
    a_values = list(map(int, input().split()))
    b_values = list(map(int, input().split()))

    test_cases.append((n, k, a_values, b_values))

# Output the result
max_experience(t, test_cases)
