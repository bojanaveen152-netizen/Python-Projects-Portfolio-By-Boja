string=input()
second_string=input()
start_index=0
Length=len(second_string)
for char in string:
    if char == second_string[start_index]:
        start_index+=1 
        if start_index == Length:
            break 
if start_index == Length:
     print("Yes")
else:
     print("No")