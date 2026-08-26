a=int(input())
b=int(input())
for i in range(a):
    if a % (a-i)==0:
        L=a-i 
        b=b-1 
    if b == 0:
      break
print(L)