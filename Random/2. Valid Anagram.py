def solve(s,t):
    freq1=[0]*26
    freq2=[0]*26
    n1=len(s)
    n2=len(t)
    if n1==n2:
        for i in range(n1):
            freq1[ord(s[i])-97]+=1
            freq2[ord(t[i])-97]+=1
    else:return False
    print(freq1,freq2)
    for i in range(26):
        if freq1[i]!=freq2[i]:
            return False
    return True
print(solve(input(),input()))
