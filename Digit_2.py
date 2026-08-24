a=int(input())
for i in range(1,a+1):
    if i == 1 or i == a:
        print("* "*a)
    elif i>1 or i<a:
        sp=(a-1)
        print("  "*sp+"*")
b=(a-1)
for p in range(1,b+1):
    if p == b:
        k=b+1 
        print("* "*k)
    else:
        print("* ")