s=input()
first_word="z"
last_word="a"
word="" 
for i in range(len(s)):
    char=s[i]
    if char!= " ":
        word +=char 
    if char==" " or i ==len(s)-1:
        if word.lower()<first_word.lower():
            first_word=word 
        if word.lower()>last_word.lower():
            last_word=word 
        word=""
first_and_last_word=first_word+ " "+last_word
print(first_and_last_word)