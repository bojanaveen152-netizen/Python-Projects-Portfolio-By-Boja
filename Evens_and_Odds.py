a=int(input())
b=int(input())
count=0
factor=0
for i in range(a,b+1):
    if i % 2 ==0:
        count=count+1
    else:
        factor=factor+1
print(factor)
print(count)