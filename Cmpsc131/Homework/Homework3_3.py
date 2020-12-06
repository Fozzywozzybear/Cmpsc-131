#Homework 3
#Aaron fosmire
#ajf434
#Collaborators Nate
rooms=[]
names=[ ]
i=0
k=0
z=0
while i < 1:

    print ('1. Reserve a room')
    print ('2. Exit')
    choice=int(input('Enter your choice:'))
    if choice == 1:
        name=input('Please enter a name:')
        Number=int(input('Please enter your desired room number: '))
    if Number in rooms:
         print ('error, please enter a room value that is not taken')
    else:
         print ( 'The room',Number, ' is reserved for',name)
         rooms.insert(z,Number)
         names.insert(z,name)
        
    if choice == 2:
        i +=1
i=0
while i < len(rooms):
    min_index=i
    j=i
    while j < len(rooms):
        if rooms[j]<rooms[min_index]:
            min_index = j 
        j+=1
    temp= rooms[i]
    rooms[i]= rooms[min_index]
    rooms[min_index] = temp

    temp = names[i]
    names[i]= names[min_index]
    names[min_index]= temp
    i+=1
i=0
print ('the reserved rooms are')
for i in range(len(rooms)):
    print ('the room',rooms[i],'is reserved for',names[i],'\n')
    
        









