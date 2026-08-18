a=int(input())
for i in range(1,a+1):
    if i==1:
        row=""
        row+="1"
        print(row)
    elif i ==a :
        for j in range(a):
            print(1+j,end=" ")
        print()
    else:
        k=(i-2)
        row="1 "+"  "*k+str(i)
        print(row)
            
