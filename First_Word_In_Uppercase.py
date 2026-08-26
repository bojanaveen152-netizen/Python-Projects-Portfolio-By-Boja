sentance=input()
st=""
store=" "
for i in sentance:
    if i == store:
        break
    upper=i.upper()
    st=st+upper
    L=len(st)
    k=sentance[L:]
print(st+k)