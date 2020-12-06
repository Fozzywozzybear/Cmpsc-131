#Homework 3
#Aaron fosmire
#Ajf434
#Collaborators None
k1=input('Enter list 1:').split()
k2=input('Enter list 2:').split()
lenk1=len(k1)//2
lenk2=len(k2)//2
k3=(k1[:lenk1]+k2[:lenk2]+k1[lenk1:]+k2[lenk2:])
print ('new list is',k3)
