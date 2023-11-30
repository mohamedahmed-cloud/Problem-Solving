import sys,math
def solve():
    freq1=[0]*60
    for i  in s1:
        if i!=" ":
            freq1[ord(i)-ord("A")]+=1
    freq2=[0]*60
    for i in s2:
        if i !=" ":
            freq2[ord(i)-ord("A")]+=1
    for i in range(60):
        if freq1[i]>=freq2[i]:
            pass
        else:
            return "NO"
    return "YES"

s1=sys.stdin.readline()
s1=s1[:-1]
s2=sys.stdin.readline()
s2=s2[:-1]
# print(s1,s2)
print(solve())
