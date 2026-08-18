a=int(input())
for i in range(1,a+1):
    if i == 1:
        sub=(a-i)
        row=" "*sub+"1"
        print(row)
    elif i == a:
        for j in range(a):
            print(1+j,end=" ")
        print()
    else:
        p=(a-i)
        b=(i-2)
        row=""
        row+=" "*p+"1 "+"  "*b+str(i)
        print(row) 
