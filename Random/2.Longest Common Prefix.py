def solve(strs):
    n=len(strs)
    to_loop=100000
    for i in strs:
        to_loop=min(to_loop,len(i))
    print(to_loop)
    s=0
    for i in range(to_loop):
        s=strs[0][:i]
        for j in strs:
            if j[:i]==s:
                pass
            else:
                return s[:i-1]
    return s
print(solve(["flow","fer","flower"]))


        