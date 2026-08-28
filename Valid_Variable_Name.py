s=input()
Valid=True 
for i in s:
    uni=(ord(i))
    valid_is=(65<=uni and 90>=uni) or (97<=uni and 122>=uni) or (48<=uni and 57>=uni)

    if not valid_is:
        Valid=False
        break 
print(Valid)