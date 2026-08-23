a=int(input())
b=int(input())
sum=a+b*(b+1)//2-1
for i in range(0,b):
    fs=i
    print("  "*fs,end="")
    for j in range(b-i):
        if i ==0 or j ==0 or j == b-i-1:
            print((sum),end=" ")
        else:
             print("  ",end="")
        sum-=1
    print()