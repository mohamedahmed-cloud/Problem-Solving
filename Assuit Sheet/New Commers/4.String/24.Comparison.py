# Time limit in test 7
import string,sys
s=list(sys.stdin.readline())
s=s[:-1]
out=s
for i in range(1,len(s)):
    a="".join(sorted(s[:i]))
    b="".join(sorted(s[i:]))
    a=a+b
    out=min(a,out)
print(out)