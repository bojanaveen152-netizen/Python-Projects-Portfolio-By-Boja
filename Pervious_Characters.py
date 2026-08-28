s=input()
word=""
for i in s:
    if i !=" ":
        word+=i
b=word 
for j in b:
    uni=(ord(j)-1)
    print(chr(uni))