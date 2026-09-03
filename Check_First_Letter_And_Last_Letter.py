string=input().split()
for i in string:
    i=i.lower()
    first=i[0]
    second=i[-1]
    if first == second:
        print("True")
    else:
        print("False")