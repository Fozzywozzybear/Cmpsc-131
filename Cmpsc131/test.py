#please enter k :3
#XOX
#oxo
#xox
k=int(input('please enter k'))
storage=['x','o']
o=" "
str2=" "
for i in range(k):
    for j in range(k):
        if j==i or i == j-2:
            o=o+storage[0]
            str2=o
        else:
            o=o+storage[1]
            str2=o
    o=''

    print (str2)
    print ("\n")
   
        

    
    

