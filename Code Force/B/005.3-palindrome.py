import sys,math
s="bbaa"
n=int(sys.stdin.readline())

out="a"
n-=1
out+=s*(n//4)+s[:n%4]
print(out)