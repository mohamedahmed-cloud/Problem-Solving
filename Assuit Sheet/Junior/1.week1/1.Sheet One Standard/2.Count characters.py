import sys,math
def solve():
    arr=[0]*58
    # print(ord("a"),ord('A'))
    for i in s:
        arr[ord(i)-65]+=1
    for i in range(58):
        if arr[i]:
            print(chr(i+65),arr[i])
s=sys.stdin.readline()
s=s[:-1]

solve()