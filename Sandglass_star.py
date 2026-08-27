a=int(input())
for i in range(0,a):
    star="* "*(a-i)
    space=" "*i 
    print(space+star)
for p in range(2,a+1):
    st="* "*p 
    sp=" "*(a-p)
    print(sp+st)