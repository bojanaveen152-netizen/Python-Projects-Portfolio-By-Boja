a=input()
count=0
c=0
for i in a:
    if i in "aeiou":
        count+=1
    elif i.isalpha():
        c+=1
print(count)
print(c)