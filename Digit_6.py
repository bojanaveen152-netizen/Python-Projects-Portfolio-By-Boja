a=int(input())
for i  in range(1,a+1):
    if i == 1 or i == a:
        print("* "*a)
    else:
        print("*")
b=(a-1)
for p in range(1,b+1):
    if p == b:
        print("* "*a)
    else:
        k=(a-2)
        print("* "+"  "*k+"*")