a=int(input())
b=int(input())
num=a 
for i in range(1,b+1):
    for j in range(1,i+1):
        if (j==1 or i ==b or i ==j ):
            print(num,end=" ")
            num=num+1
        else:
             print("  ",end="")
    print()