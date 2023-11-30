import sys,math
s=sys.stdin.readline()
s=s[:-1]
t=sys.stdin.readline()
t=t[:-1]
i=0
j=0
count=1
while i<len(s) and j<len(t):
    if s[i]==t[j]:
        count+=1
        i+=1
    j+=1
print(count)