def DP(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    res = [[0] * (n2 + 1) for i in range(n1 + 1)]

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):

            if s1[i - 1] == s2[j - 1]:
                res[i][j] = 1 + res[i - 1][j - 1]
            else:
                res[i][j] = max(res[i][j - 1], res[i - 1][j])


    print(res)
    return res[n1][n2]

s1 = "abcba"
s2 = "abcbcba"
print(DP(s1, s2))
