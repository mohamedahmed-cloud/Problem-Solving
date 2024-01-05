def LCS(i, j):
    if (i >= l[0] or j >= l[1]):
        return 0

    if s1[i] == s2[j]:
        return 1 + LCS(i + 1, j + 1)

    else:
        return max (LCS(i + 1, j), LCS(i, j + 1))

s1 = "abcdf"
s2 = "abcdefdef"
l = [len(s1), len(s2)]
print(LCS(0, 0))

