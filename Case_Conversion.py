a=input()
result=""
for i in range(len(a)):
    if a[i].isupper():
        if i!=0:
            result+="_"
        result+=a[i].lower()
    else:
        result+=a[i]
print(result)