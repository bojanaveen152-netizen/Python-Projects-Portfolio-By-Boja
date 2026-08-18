a=int(input())
for i in range(1,a+1):
    sp=(a-i)
    if i == 1:
        row=""
        row+=" "*(sp)+"5"
        print(row)
    elif i==a:
        p=5
        for j in range(a):
            print(p,end=" ")
            p=p+1
        print()
    else:
        b=(2*a-1)-((2*sp))-2
        mi=" "*b 
        row=" "*sp+"5"+" "*b+str(5+i-1)
        print(row)
