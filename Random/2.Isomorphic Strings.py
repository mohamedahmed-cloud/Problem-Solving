def solve(s,t):
    from collections import defaultdict
    our_dict1 = defaultdict()
    our_dict2=defaultdict()
    n1=len(s)
    n2=len(t)
    if n1!=n2:
        return False
    for i in range(n1):
        our_dict1[t[i]]=s[i]
        our_dict2[s[i]]=t[i]
    compare1=""
    compare2=""
    # print(our_dict1)
    for i in range(n1):
        compare1+=our_dict1[t[i]]
        compare2+=our_dict2[s[i]]
    # print(compare1)
    if compare1==s and compare2==t:
        return True
    return False
print(solve("ffi","fii"))