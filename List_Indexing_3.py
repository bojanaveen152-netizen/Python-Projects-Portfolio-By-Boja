N=int(input())
T=int(input())
list_a=[]
for i in range(N):
    number=int(input())
    list_a+=[number]
index=list_a  
for j in range(T):
    K=int(input())
    print(index[K])