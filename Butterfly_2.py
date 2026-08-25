a=int(input())
for i in range(1,a+1):
    b="* "*i 
    ms=2*(a-i)
    print(b+"  "*ms+b)
for p in range(0,a+1):
    k=(a-p)
    c="* "*k
    md=(2*p)
    print(c+"  "*md+"* "*k)