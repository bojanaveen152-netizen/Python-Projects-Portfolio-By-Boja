a=int(input())
for i in range(1,a+1):
    if i ==1 or i == a:
        print("* "*a) 
    else:
        p=(a-1)
        print("  "*p+"*")
for j in range(1,a):
    if j == (a-1):
        print("* "*a)
    else:
        print("  "*p+"*")