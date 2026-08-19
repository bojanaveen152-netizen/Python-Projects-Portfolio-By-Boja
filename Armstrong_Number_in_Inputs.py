a=int(input())
for i in range(1,a+1):
    b=int(input())
    L=len(str(b))
    sum=0
    for j in str(b):
        add=int(j)**L 
        sum=sum+add 
    if sum == b:
           print(b)