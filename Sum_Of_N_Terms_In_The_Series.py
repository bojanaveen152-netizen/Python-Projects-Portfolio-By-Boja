X=float(input())
N=int(input())
sum=0
for i in range(1,N+1):
    b=(X) ** i
    sum+=b 
print(round(sum,4))