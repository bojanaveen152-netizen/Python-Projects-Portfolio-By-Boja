N=int(input())
S=input()
sum=0
for i in range(1,N+1):
    b=float(input())
    sum+=b
equal=(round(sum,N))
print(equal==float(S))