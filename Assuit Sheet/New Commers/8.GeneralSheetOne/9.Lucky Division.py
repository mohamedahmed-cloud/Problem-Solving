n=int(input())
if n%7==0 or n%4==0 or n%74==0 or n%47==0 or n%447==0 or n%774==0 or n%477==0 or n%744==0:
    print("YES")
    quit()

arr=str(n)
for i in arr:
    if i!="4" and i !="7":
        print("NO")
        quit()
print("YES")