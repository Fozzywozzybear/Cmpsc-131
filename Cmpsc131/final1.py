list1=(input('please enter list'))
list2=(input('please enter list 2'))
t=list1.split()
l1=[int(x) for x in t]
t=list2.split()
l2=[int(x) for x in t]

list3=[]
i=0
while i < len(l1):
    list3.append(l1[i])
    list3.append(l2[i])
    i+=1
print( ' the new list is',end="")
for i in list3:
    print(i,end=" ")
