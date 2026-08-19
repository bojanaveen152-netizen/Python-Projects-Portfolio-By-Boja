a=int(input())
for i in range(1,a+1):
    if i==1 or i ==a:
        for j in range(0,a):
            print(str(a-j),end=" ")
        print()
    else:
        p=(a-2)
        print(str(a)+" "+"  "*p+str("1"))
