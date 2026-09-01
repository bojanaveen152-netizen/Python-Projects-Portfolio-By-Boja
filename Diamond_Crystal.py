a=int(input())
for i in range(1,a+1):
    Left_spaces=" "*(a-i)
    middle_spaces="  "*(i-1)
    print(Left_spaces+"/"+middle_spaces+"\\")
for j in range(1,a+1):
    F_spcaes=" "*(j-1) 
    M_spaces="  "*(a-j)
    print(F_spcaes+"\\"+M_spaces+"/")