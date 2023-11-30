def solve(s,t):
    k=0
    n=len(s)
    if n==0:return True
    for i in t:
        if s[k]==i:
            k+=1
        if k==n:
            return True
    return False

print(solve("","aaa"))