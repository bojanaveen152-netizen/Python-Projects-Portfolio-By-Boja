a=int(input())
b=int(input())
sp=2*b-3
for i in range(1,b+1):
    row=""
    for j in range(1,b+1):
        if i ==1 or i ==b:
            row+=str(a)+" "
        else:
            row=str(a-b+1)+" "*sp+str(a)
        a+=1
    print(row)