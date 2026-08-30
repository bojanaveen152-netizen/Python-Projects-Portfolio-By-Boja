a=int(input())
for i in range(0,a):
    stars=(a-i)
    spaces=(2*i)
    if stars == a:
        print("* "*(stars+stars))
    elif stars < a:
        print("* "*stars+"  "*spaces+"* "*stars)
for i in range(1,a):
    stars_2=(i)
    spaces_2=(2*a-i-i)
    print("* "*stars_2+"  "*spaces_2+"* "*stars_2)
print("* "*(a+a))