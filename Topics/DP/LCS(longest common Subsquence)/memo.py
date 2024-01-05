def LCS(i, j, memo):
    if (i >= l[0] or j >= l[1]):
        return 0

    if (i, j) in memo:
        return memo[(i, j)]

    if s1[i] == s2[j]:
        memo[(i, j)] = 1 + LCS(i + 1, j + 1, memo)
        return memo[(i, j)]

    else:
        memo[(i, j)] = max (LCS(i + 1, j, memo), LCS(i, j + 1, memo))
        return memo[(i, j)]

s1 = "f"
s2 = "abcdefdef"
l = [len(s1), len(s2)]
print(LCS(0, 0, {}))

