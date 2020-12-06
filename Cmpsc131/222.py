
Counter=1
N=int(input('Please entner a number'))
storage = 2*N-1
for i in range (2*N-1):
    print ("\n")
    for J in range (N-Counter):
        print ('*',end="")
    for X in range (Counter):
        print (Counter,end="")
    if i<N-1:
        Counter += 1
    else: 
        Counter -= 1 
