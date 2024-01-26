from collections import Counter
two_d_array = [[3,1,2,2],[1,4,4,4],[2,4,2,2],[2,5,2,2]]
l = zip(*two_d_array)
l = Counter(l)
ans = 0

for i in two_d_array:
        ans += l[tuple(i)]

print(l, ans)
