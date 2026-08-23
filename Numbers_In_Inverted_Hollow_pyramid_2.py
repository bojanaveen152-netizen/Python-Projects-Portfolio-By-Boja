a=int(input())
b=int(input())
num=a
for i in range(b):
    print(" "*i,end="")
    for j in range(b-i):
        if i==0 or j==0 or j==b-i-1: 
          print(num,end=" ")
        else:
            print(" ",end=" ")
        num+=1
    print()