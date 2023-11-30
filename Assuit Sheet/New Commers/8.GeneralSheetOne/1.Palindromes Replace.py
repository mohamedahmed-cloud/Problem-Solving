import sys,math
string=sys.stdin.readline()
string=list(string)
string=string[:-1]
length=len(string)
for i in range(length):
    if string[i] == '?':
        if string[i]==string[length-i-1]:
            string[i]="a"
        else:
            string[i]=string[length-i-1]

concat=""
for i in  range(length-1,-1,-1):
    concat+=string[i]
if string==list(concat):
    print(concat)
else:print(-1)