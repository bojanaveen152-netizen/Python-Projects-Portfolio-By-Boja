def count_of_lowercase_and_uppercase_letters(arg_1):
    count_lower=0
    count_upper=0
    for i in word:
        if i.isupper():
            count_upper+=1 
        elif i.islower():
            count_lower+=1 
    print(count_upper)
    print(count_lower)
word = input()
result=count_of_lowercase_and_uppercase_letters(arg_1=word)