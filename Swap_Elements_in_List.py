L = [1, "two", 9, 5.09, "Three", -558, "four", -93.7, "six"]

a=int(input())
b=int(input())
list_a=L[a] 
list_b=L[b] 
L[a]=list_b
L[b]=list_a
print(L)
