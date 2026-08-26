a=int(input())
b=int(input())
for i in range(1,b+1):
    numbers=i 
    if a % i == 0 and b % i ==0 :
        greatest=i 
    if greatest>=1:
        c=greatest
    if a % c ==0 and b % c==0:
        k=c 
print(k)