#aaron fosmire
#ajf434
#homework 4
#collaborators Nate Malay 

def factors(k):
    for i in range (1,k):
        if k % i==0:
            arr.append(i)
            
def prime(arr):
    i=0
    j= len(arr)
    for i in range(j-1):
        if arr[i] % (i+1) == 0:
            arr.pop(i)
arr=[]
j=0
k=int(input('please enter k: '))
factors(k)
prime(arr)
print (arr)

