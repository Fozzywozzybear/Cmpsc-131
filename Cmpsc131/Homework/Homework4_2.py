#aaron fosmire
#homework 4 pt 2
#Collabs None
#ajf434

def absolute(z,i):
    x=abs(z[i])
             
    return (x)            
           
z=list()         
list1=[int(x) for x in input('please enter').split()]

p=0
for i in range(len(list1)):
    z.append(list1[i])
i=0
for i in range(1,len(z)):
    if z[i]<0:
        for j in range(len(z)):
            if absolute(z,i)<=z[j]:
                temp=z[j]
                z[j]=z[i]
                z[i]=temp
    else:
        for j in range(len(z)):
            if z[i]<z[j]:
                temp=z[j]
                z[j]=z[i]
                z[i]=temp
                
                        
    
    
                    
                      
                      

'absolute(list1)'
                      
print (z)
        
"""
take a list as input
sort list by numbers
compare the negative to the postive is there is one
"""
