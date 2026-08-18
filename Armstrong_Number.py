a=int(input())
b=int(input())
found=False
for i in range(a,b+1):
    L=len(str(i))
    sum=0
    for digit in str(i):
        k=int(digit)
        p=(k**L)
        sum=sum+p 
    if sum==i:
        print(i,end=" ")
        found=True
if not found:
    print("-1")
