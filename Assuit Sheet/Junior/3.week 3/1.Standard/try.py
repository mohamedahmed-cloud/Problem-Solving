a=[1,2,3]
b=[5,6,7]
c=[10,20,30]
x=zip(a,b,c)
print(list(x))
for i in zip(a,b,c):
    print(i)