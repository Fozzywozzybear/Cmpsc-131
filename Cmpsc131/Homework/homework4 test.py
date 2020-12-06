def absolute(lst,j):
    tmp=abs(lst[j])
    return (tmp)
lst=list()
k=[int(x) for x in input('please enter a list: ').split()]
for i in range (len(k)):
    lst.append(k[i])
    print (lst)
for j in range(i+1,len(lst)):
    if lst[j] < 0:
        for z in range(len(lst)):
            if absolute(lst,j)==lst[j-z]:
                temp=lst[j-1]
                lst[j]=lst[j-1]
                lst[j-1]=temp
    else:
        if lst[j]<lst[j-1]:
            temp=lst[j-1]
            lst[j]=lst[j-1]
            lst[j-1]=temp
            
            
print (lst)
    
    
