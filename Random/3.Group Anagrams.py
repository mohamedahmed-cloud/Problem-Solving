def solve(strs):
    out=[]
    sorted_string=[]
    def inlist(x,sorted_string):
        for i,value in enumerate(sorted_string):
            if value==x:
                return i
        return -1
    for i in strs:
        x="".join(sorted(list(i)))
        b=inlist(x,sorted_string)
        if b==-1:
            sorted_string.append(x)
            out.append([i])
        else:
            out[b].append(i)
    return out

    

print(solve(["eat","tea","tan","ate","nat","bat"]))