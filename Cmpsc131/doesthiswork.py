def checker1(n):
    checked= False
    store=0
    arr=[]
    if n >= 10:
        for i in range (n):
            store=n%10
            arr.append(arr[store])
            n=n//10
            store=0
    else:
        arr.append(n)
    k=arr
    while checked == False :
        for i in range (k):

            if arr[i] >= arr[i+1] and arr[i-1]:
                checked == False
            else:
                checked == True
    return (checked)

def main(checked):

    if checked == False:
        print ('valid')
    else:
        print ('not valid')

n=int(input('please enter n'))
checker1(n)
main()
    
