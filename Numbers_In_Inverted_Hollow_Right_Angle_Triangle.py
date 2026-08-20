a=int(input())
num=1 
for i in range(a):
    for j in range(a-i):
        if i ==0 or j == 0 or j==a-i-1:
           print(num,end=" ")
        else:
           print(" ",end=" ")
        num=num+1
    print()