import sys,math
t=int(sys.stdin.readline())
stack=[]
count=0
ans="ACC"
for i in range(t):
    s=sys.stdin.readline().strip()
    if s=="Header" or s=="EndHeader":
        count+=1
    if ans=="ACC":
        if i==0:
            if s=="Header":
                stack.append(s)
            else:
                ans="WA"
        elif i==t-1:
            if s!="EndHeader":
                ans="WA"
        elif s[:3]=="End":
            if stack and stack[-1]==s[3:]:
                stack.pop()
            else:
                ans="WA"
        elif s[:3] !="End":
            stack.append(s)
if count==2:
    print(ans)
else:print("WA")

            

        
