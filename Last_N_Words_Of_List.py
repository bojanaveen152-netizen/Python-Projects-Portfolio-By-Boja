string=input().split()
number=int(input())
store=[]
for i in string:
    store+=[i]
    p=store[::-1]
print(p[:number])