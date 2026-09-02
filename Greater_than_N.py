num_list = [1, 6, 32, 93, 71, -20, 30, -90, 50]
number=int(input())
store=[]
for i in num_list:
    change_int=int(i)
    if change_int > number:
        greater=change_int 
        store+=[greater] 
print(store)