number=input()
list_a=number.split()
store=[]
for i in list_a:
    i=int(i)
    if (i) % 3 == 0:
        store+=[i]
print(store)