a=int(input())
number=input().split()
length=len(number)
for i in range(length):
    number[i]=int(number[i])
if a % 2==0:
    half= a // 2
else:
    half= a//2+1
print(number[half:])