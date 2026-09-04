string=input().split()
length=len(string)
if length % 2 ==0:
    half=length//2
else:
    half=length//2+1 
new=string[:half]
print(new)