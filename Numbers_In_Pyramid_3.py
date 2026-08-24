a=int(input())
for i in range(1,a+1):
    row=i 
    leftz=(a-i)
    ones=(2*i-1)
    print("0 "*leftz+"1 "*ones+"0 "*leftz)