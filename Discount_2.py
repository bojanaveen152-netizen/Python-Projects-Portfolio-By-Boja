def get_discount(amount):
    # Complete this function
    if (amount < 500):
        print("5%")
    elif (amount>=500 and amount<2500):
        print("10%")
    elif (amount>=2500):
        print("20%")
amount = int(input())
# Call the get_discount function
integer=get_discount(amount)