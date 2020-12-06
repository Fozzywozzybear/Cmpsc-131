rooms=[]
k=0
i=0

while i < 1:

    print ('1. Reserve a room')
    print ('2. Exit')
    choice=int(input('enter your choice'))
    if choice == 1:
        name=input('please enter your name')
        number=int(input('please enter your desired room number'))
        print ('the room', number,'has been reserved for',name)
        rooms.insert(number,name)
    else:
        print ('Room has been reserved')
    if choice == 2:
        i +=1
print ('the reserved rooms are')
for i in range(len(rooms)):
    st=rooms[i]
    print (st,('\n'))
    print (rooms.index(st))
           
