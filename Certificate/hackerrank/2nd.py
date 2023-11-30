def solve(s,k):
    ans = ["Not found!"]
    res = 0
    for i in range(len(s)-k+1):  
        my_sum = 0  
        my_arr = s[i:i+k]
        for i in "aeiou":
            my_sum += my_arr.count(i) 
        if res < my_sum:
            ans = my_arr
            res = my_sum
    return "".join(ans)
print(solve(input(),int(input())))