import sys,math
t=int(sys.stdin.readline())
for i in range(t):
    arrX1=[]
    arrY1=[]

    arrX2=[]
    arrY2=[]
    n=int(sys.stdin.readline())
    first_compare=[-10e6,-10e6]
    second_compare=[10e7,10e7]
    arr1=[]
    arr2=[]
    for j in range(n):
        x1,y1,x2,y2=map(int,sys.stdin.readline().split())
        arr1.append([x1,y1])
        arr2.append([x2,y2])
        if x1==0 and y1==0 and x2==0 and y2==0:
            ans=0
        else:
            # First compare
            if x1>first_compare[0]:
                first_compare[0]=x1
            if y1>first_compare[1]:
                first_compare[1]=y1
            # Second compare
            if x2<second_compare[0]:
                second_compare[0]=x2
            if y2<second_compare[1]:
                second_compare[1]=y2
            width=abs(first_compare[0]-second_compare[0])
            height=abs(first_compare[1]-second_compare[1])
            ans=width*height
        # check if there are no intersections
        if second_compare[0]>first_compare[0] and second_compare[1]>first_compare[1]:
            pass
        else:ans=0

    print(f"Case #{i+1}: {str(ans)}")
