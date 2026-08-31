string=input()
store=""
for i in range(len(string)):
    if i == 0:
        store+=chr(ord(string[i])+1)
    elif string[i-1]==" ":
        store+=chr(ord(string[i])+1)
    else:
        store+=string[i] 
print(store)