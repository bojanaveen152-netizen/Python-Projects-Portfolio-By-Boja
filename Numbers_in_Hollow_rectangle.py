a=int(input())
b=int(input())
k=a*b 
h=b-2
for i in range(a):
    each=""
    if i == 0 or i == a-1:
        for j in range(b):
            each=each+str(k)+" "
            k=k-1
    else:
        each=str(k)+" "
        k=k-h-1
        each=each+"  "*(h)+str(k)
        k=k-1
    print(each)
            