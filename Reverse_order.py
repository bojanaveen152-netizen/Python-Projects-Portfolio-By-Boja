a=int(input())
list_a=[]
for i in range(a):
    string=input()
    list_a+=[string]
for j in range(a):
    print(list_a[a-j-1])