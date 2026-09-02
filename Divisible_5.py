N=int(input())
store=[]
for i in range(1,N+1):
    number=int(input())
    if number % 5 == 0:
        store.append(number)
print(store)