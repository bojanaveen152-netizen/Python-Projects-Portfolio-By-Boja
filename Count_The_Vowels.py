def count_the_vowels(word):
    count=0
    for i in word:
        is_a = i == "a"
        is_e = i == "e"
        is_i = i == "i"
        is_o = i == "o"
        is_u = i == "u"
        is_vowels=((((is_a or is_e) or is_i) or is_o) or is_u)
        if is_vowels:
            count+=1
    return count


word = input()
result=count_the_vowels(word)
print(result)