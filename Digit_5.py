a=int(input())
for i in range(1,a+1):
    if i == 1 or i == a:
        print("* "*a)
    else:
        print("*")
b=(a-1)
for c in range(1,b+1):
    if c==b:
        print("* "*a)
    else:
        print("  "*b+"*")