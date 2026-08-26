N=int(input())
first=0 
for i in range(N):
    b=int(input())
    if b>1:
        is_prime=True 
        for j in range(2,b):
            if b % j ==0:
                is_prime=False 
                break 
        if is_prime and first==0:
            first=b 
print(first)