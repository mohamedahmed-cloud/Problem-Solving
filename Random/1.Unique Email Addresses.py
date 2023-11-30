def solve(emails):
    ans=set()
    for i in emails:
        to_add=""
        plus=0
        after=0
        for j in i:
            if j=="@":
                after="@"
            if j=="." and after==0:
                pass
            elif j=="+":
                plus="+"
            elif plus==0 or after=="@":
                to_add+=j
        ans.add(to_add)
    return len(ans)
print(solve(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))