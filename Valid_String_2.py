def valid_string(string):
    S=len(string)
    A=string[0] 
    if (S>=6)  or  A.isdigit():
        print("Valid String")
    else:
        print("Invalid String")

string = input()
result = valid_string(string)