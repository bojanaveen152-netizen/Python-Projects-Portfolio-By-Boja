a=int(input())
for i in range(1,a+1):
    spaces=" "*(a-i)
    m_s=" "*(2*i-3)
    if i == 1:
        print(spaces+"A")
    if i > 1:
        print(spaces+chr(65+i-1)+m_s+chr(65+i-1))
for j in range(1,a):
    Fspaces=" "*(j)
    mspaces=" "*(2*(a-j)-3)
    if j == a-1:
        print(Fspaces+"A")
    else:
        le=(chr(65+a-j-1))
        print(Fspaces+le+mspaces+le)