a=int(input())
b=int(input())
for i in range(1,a+1):
    p=(i-1)
    if i ==1:
        for j in range(0,a):
            print(str(b+j),end=" ")
        print()
    elif i==a:
        row=""
        row+=" "*p+str(b)
        print(row)
    else:
        sub=((2*(a-i)))
        sub=sub-1
        f=b+j
        print(" "*p+str(b)+" "*sub+str(f-i+1))
        f=f-1
    