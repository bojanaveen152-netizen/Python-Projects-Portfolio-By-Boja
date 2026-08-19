a=int(input())
for i in range(1,a+1):
    sp=(i-1)
    if i == 1:
        for j in range(1,a+1):
            print(str(j),end=" ")
        print()
    elif (i>1 and i<a):
        md=(a-i-1)
        print(" "*sp+str("1")+" "+"  "*md+str(a-i+1))
    else:
        print(" "*sp+"1")