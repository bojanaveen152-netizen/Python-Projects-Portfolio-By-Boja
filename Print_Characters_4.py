S=input()
M=int(input())
N=int(input())
store=""
for i in S:
    uni=(ord(i))
    if M<=uni<=N:
        store+=(chr(uni)+" ")
print(store)