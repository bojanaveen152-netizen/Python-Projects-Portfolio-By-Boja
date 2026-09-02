N=int(input())
list_a=[]
for i in  range(1,N+1):
    number=int(input())
    list_a+=[number]
list_c=(list_a[0:2])
list_b=(list_a[-2:])
print(list_c+list_b)