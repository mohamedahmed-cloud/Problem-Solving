def solve(numRows):
    x=[[1],[1,1]]
    if numRows==1:
        return [x[0]]
    elif numRows==2:
        return x
    else:
        for i in range(numRows-2):
            f=x[-1]
            length=len(x[-1])
            newx=[1]
            for i in range(1,length):
                newx.append(f[i-1]+f[i])
            newx.append(1)
            x.append(newx)
    return x
print(solve(2))