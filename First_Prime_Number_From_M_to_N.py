a=int(input())
b=int(input())
st=""
for i in range(a,b+1):
    count=0
    if i > 1:
      for j in range(2,b+1):
        if i % j ==0:
         count=count+1
    if count == 1:
        print(i)
        break
else:
        print("No prime numbers in the given range")