def calculate_percentage(number):
    if (number<1000):
        result=((5/100)*number)
    elif (number>=1000):
        result=((10/100)*number)
    return result
number = int(input())
result = calculate_percentage(number)
print(result)