a=int(input())
for i in range(1,a+1):
    for j in range(1,i+1):
        if i==1 or j==1:
           row=""
           row +=" "*(a-i)+str(j)+" "
        elif i==a or j==a:
            row+=" "*(a-i)+str(j)+" "
        else:
            row+=str(j)+" "
    print(row)
