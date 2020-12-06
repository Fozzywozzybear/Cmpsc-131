#Homework 2
#Aaron fosmire
#ajf434
#Collaborators: Nate Dreyer

n=int(input('please enter a number'))
storage=0
N=n
reverse=0
while n > 0:
    storage= n%10
    reverse = reverse * 10 + storage
    n = n//10
if (N == reverse ):
    print ('same')
elif (reverse != N):
    print ('not the same')
    
