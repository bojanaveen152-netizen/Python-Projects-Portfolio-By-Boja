string=input()
list_a=string.split()
result=[]
for i in list_a:
    if (len(i)>2):
        charcter=i[2]
    result+=charcter
join=",".join(result)
print(join)