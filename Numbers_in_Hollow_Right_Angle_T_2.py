a=int(input())
for i in range(1,a+1):
    sp=a-i 
    if i == 1:
        row=""
        row+="  "*sp+"1"
        print(row)
    elif i==a:
        for j in range(a):
            print(a-j,end=" ")
        print()
    else:
        d=i 
        if d>1:
            st=d-2
            row=""
            row+="  "*sp+str(i)+"  "*st+" 1"
            print(row)
