T=input()
number=int(T[:-1])
if T[-1] == "M":
    hours=number/60
else:
    hours=number/3600
print(str(round(hours,2))+"H")