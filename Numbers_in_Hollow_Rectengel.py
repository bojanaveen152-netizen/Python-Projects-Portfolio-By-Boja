a=int(input())
b=int(input())
for i in range(1,a+1):
    if i ==1 :
        for j in range(b):
            c=7
            print(str(c+j),end=" ")
        print()
    elif i == a:
        for j in range(b):
            c=7
            print(str(c+j),end=" ")
        print()
    else:
        sp=a
        coloum=(b-2)
        print(str(c)+" "+"  "*coloum+str(c+j))
