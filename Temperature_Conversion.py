a=input().strip()
num=a[-1]
tem=float(a[:-1])
if num == "C":
    c=tem 
    f=c*9/5+32
    k=c+273 
elif num == "F":
    f=tem 
    c=(f-32)*5/9 
    k=c+273
elif num=="K":
    k=tem
    c=k-273
    f=c*9/5+32
    
print(f"{round(c, 2)}C")
print(f"{round(f, 2)}F")
print(f"{round(k, 2)}K")