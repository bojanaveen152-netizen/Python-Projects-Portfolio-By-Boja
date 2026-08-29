a=int(input())
for i in range(1,a+1):
    space=a-i 
    star=(2*i-1)
    print(". "*space+"0 "*star+". "*space)
for j in range(1,a):
    spaes_2=j
    star2=(2*a-j-j-1) 
    print(". "*spaes_2+"0 "*star2+". "*spaes_2)