a=int(input())
store=[]
for  i in range(1,a+1):
    b=input()
    store+=[b]
indexing=store[0:3]
indexing_2=store[-3:]
print(indexing+indexing_2)