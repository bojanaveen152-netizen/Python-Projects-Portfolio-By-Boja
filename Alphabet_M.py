a=int(input())
for i in range(1,a+1):
    space_1=" "*(a-i)
    middle_1=" "*(2*i-2-1)
    space_2=" "*(2*a-i-i)
    if i == 1:
        print(space_1+chr(65)+space_2+" "+chr(65))
    if i >1:
        print(space_1+chr(64+i)+middle_1+chr(64+i)+" "+space_2+chr(64+i)+middle_1+chr(64+i))