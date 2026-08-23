a=int(input())
for i in range(1,a+1):
    sp=(a-i)
    if i == 1:
        print(" "*sp+str(i))
    else:
        p=(2*i-3)
        print(" "*sp+str("1")+" "*p+str(i))
for b in range(1,a):
    ss=b
    if b<a-1:
       fs=(a-b)
       md=(2*fs-3)
       print(" "*ss+str("1")+" "*md+str(fs))
    else:
        print(" "*ss+"1")