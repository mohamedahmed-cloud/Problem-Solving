
import sys,math
def solve(k,n,s):
    freq=[0]*26
    for i in range(n):
        freq[ord(s[i])-ord('a')]+=1
    a=97
    # print(freq)
    if n==k:
        return ""
    else:
        for i in range(26):
            # try:
                s=s.replace(chr(a),"",min(k,freq[a-ord('a')]))
                k-=min(k,freq[a-ord('a')])
                if k==0:
                    break
                else:
                    a+=1
    return s
            # except:
            #     pass

n,k=map(int,sys.stdin.readline().split())
s=sys.stdin.readline()
s=s[:-1]
a=solve(k,n,s)
print(a)
