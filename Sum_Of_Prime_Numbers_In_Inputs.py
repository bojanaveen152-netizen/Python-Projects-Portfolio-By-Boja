a=int(input())
fact=0
for i in range(1,a+1):
    b=int(input())
    num=0
    for j in range(2,b):
        if b % j ==0 :
            num+=1
    if num == 0 and b>1:
      fact+=b
print(fact)