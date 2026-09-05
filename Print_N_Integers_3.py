def say_wishes(arg_1):
    greet="Welcome "+arg_1
    return greet

name=input()
greet=say_wishes(arg_1=name)
print(greet)