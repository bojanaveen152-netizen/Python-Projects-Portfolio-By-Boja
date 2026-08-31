String=input()
store=""
for i in String:
    if i != " ":
        uni=ord(i)
        inc=int(uni+1)
        Con_Char=(chr(inc))
        store+=(Con_Char)
    else:
        store+=i
print(store)