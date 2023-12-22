import math
ans = 0
for i in range(3):
    ans += math.gcd(i, 3)
for i in range(4):
    ans += math.gcd(i, 4)
print(ans)
print(math.gcd(3, 4))