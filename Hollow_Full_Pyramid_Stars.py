a=int(input())
for i in range(1,a+1):
    sp=(a-i)
    if i == 1:
        print(" "*sp+"*")
    elif i == a:
        print(" "*sp+"* "*a)
    else:
        b=(i-2)
        print(" "*sp+"* "+"  "*b+"*")
