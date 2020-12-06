#Homework2
#Aaron fosmire
#ajf434
#Collaborators: None
Counter=1
n=int(input('please enter a number'))
index= 2*n-1
for i in range (2*n-1):
    print("\n")
    for J in range (n-Counter):
        print ('*',end="")

    for X in range (Counter):
        print (Counter,end="")

    if i<n-1:
        Counter +=1
    else:
        Counter -= 1
        
        
        
