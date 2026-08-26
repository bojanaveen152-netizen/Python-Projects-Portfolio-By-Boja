a=int(input())
b=65
st=""
for i in range(1,a+1):
    for j in range(i,i+1):
        st=st+chr(b)+" "
        print(st)
    b=b+1
print()