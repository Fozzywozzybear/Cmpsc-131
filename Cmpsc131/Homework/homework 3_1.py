#homework 3
#Aaron fosmire
#ajf434
#Collaborators Teshi Nate


arr=[1,2,3]
k=int(input('please enter k:'))
i=1
if k >= 3 :
    for i in range (k) :
        arr.append(arr[i]+arr[i+1]+arr[i+2])
print (arr[k])
          
        


