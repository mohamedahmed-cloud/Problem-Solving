import sys,math
main=sys.stdin.readline().strip()
x=sys.stdin.readline().strip()
toOut=sys.stdin.readline().strip()
l={}
s=""
for i in range(26):
    l[main[i].lower()]=x[i].lower()
    l[main[i].upper()]=x[i].upper()
for i in toOut:
    try:
        s+=l[i]
    except:
        s+=i
print(s)

