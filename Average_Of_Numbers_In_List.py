number=input().split()
Length=len(number)
add=0
for i in number:
    add+=int(i)
total=add/int(Length)
print(round(total,2))