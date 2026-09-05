def validate_atm_pin_code(pin):
    length=len(pin)
    if pin.isdigit() and (length==4 or length==6):
        result="Valid PIN Code"
    else:
        result="Invalid PIN Code"
    return result