def calculate_bill(amount):
    if (amount<500):
        result=amount-(amount*5/100)
    elif (amount>=500 and amount<2500):
        result=amount-(amount*10/100)
    elif (amount>=2500 ):
        result=amount-(amount*20/100)
    return result
amount = int(input())
result=calculate_bill(amount)