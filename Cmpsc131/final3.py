n = int(input("please enter n"))

nos=1
while nos<=n:
    ns=n-nos
    half=ns//2
    print(half*"*",end="")
    print(nos*"o",end="")
    print(half*"*")
    nos+=2

nos = n-2
while nos >= 1:
    ns = n-nos
    half = ns//2
    print(half*"*",end="")
    print(nos*"o",end="")
    print(half*"*")
    nos -= 2
