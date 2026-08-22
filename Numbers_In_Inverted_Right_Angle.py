a=int(input())
num=a*(a+1)//2
for i in range(1,a+1):
    for j in range(a-i+1):
        if i ==1 or j==0 or j==a-i:
          print(num,end=" ")
        else:
            print(" ",end=" ")
        num-=1
    print()