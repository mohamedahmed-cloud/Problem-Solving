import sys,math
s=sys.stdin.readline()
s=s[:-1]
ans=len(s)
one=0
two=0
for i in s:
    if i =="(" :
        one+=1
    elif i==")" and one>0:
        one-=1
    else:
        # print(one)
        two+=1
# print(one,two)
print(ans-(one+two)) 
# another solution.
import sys,math
s=sys.stdin.readline().strip()
stack=0
all=len(s)
not_append=0
for i in s:
    if i=="("  :
        stack+=1
    elif i==")" and stack:
        stack-=1
    else:
        not_append+=1
print(all-not_append-stack)
    