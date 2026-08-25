a=int(input())
b=int(input())
c=65
for i in range(a):
    for j in range(b):
        if i ==0 or i ==a-1 or j==0 or j ==b-1:
            print(chr(c),end=" ")
        else:
            print(" ",end=" ")
        c+=1
    print()