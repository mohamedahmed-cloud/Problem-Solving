import sys,math
def solve(s):
    for i in s:
        i=i.lower()
        freq[ord(i)-ord('A')]=1
n=int(sys.stdin.readline())
s=sys.stdin.readline()
freq=[0]*60
solve(s)
a=freq.count(1)
# print(a)
if a>26:
    print("YES")
else:print("NO")