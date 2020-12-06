#Homework 2
# Aaron fosmire
#ajf434
#Collaborators None
n=int(input('Enter n '))
Number=0
Storage=(n*(n+1))//2
for i in range (n-1):
    print ("please enter a unique number between 1 and ",n,end =" ")
    Number=int(input())
    Storage=Storage - Number

print ('the missing number is ',Storage)
