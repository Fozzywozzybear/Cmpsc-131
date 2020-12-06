# Assignment 3
#aaron fosmire
#ajf434
#Collaboratos Teshi,Nate D, Joe M,Zach P.
k=int(input('please enter k'))
storage=['x','o']

for i in range(k):
    str1=""
    for j in range(k):
        if j==i or j == k-i-1:
            str1=str1+storage[0]
            
        else:
            str1=str1+storage[1]
            
    

    print (str1)
   
        

    
    

