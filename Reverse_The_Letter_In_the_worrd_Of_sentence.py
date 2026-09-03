string=input().split()
store=[]
for i in string:
    store+=i[::-1]+" "
join="".join(store)
print(join)