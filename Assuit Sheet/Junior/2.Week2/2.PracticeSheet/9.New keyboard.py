import sys,math,bisect
for i in range(5):
    s=sys.stdin.readline().strip()
    for i,value in enumerate(s):
        if value=="[":
            s=s[i+1:]+s[:i]
        elif value=="]":
            s=s[i+1:]+s[:i]