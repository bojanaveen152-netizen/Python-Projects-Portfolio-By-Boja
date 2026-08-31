Letter=input()
store=""
for char in Letter:
    store+=char+"-"
store=store 
length=len(store)-1
print(store[:length])