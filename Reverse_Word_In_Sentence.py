number=input().split()
length=len(number)
for i in range(length):
    number[i]=int(number[i])
if length % 2 ==0 :
    half= length // 2
else:
    half=length//2+1 
first=number[:half]
print(first)