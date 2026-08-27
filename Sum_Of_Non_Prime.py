a=int(input())
fount=0
for i in range(1,a+1):
    b=int(input())
    count=0
    for j in range(2,b):
        if b % j ==0:
           count+=1
    if count>0:
        fount+=b 
print(fount)