s=input()
store=""
for char in s:
    store+=char+","
last=len(store)
print(store[:-1])