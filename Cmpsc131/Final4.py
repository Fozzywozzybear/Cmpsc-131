A = input("Please enter the numbers to sort: ")
B = input("Please enter the positions which remain fixed :")
t = A.split()
a = [int(x) for x in t]
t = B.split()
b = [int(x)-1 for x in t]
tosort = []
nottosort = []
i = 0
while i < len(a):
    if i in b:
        nottosort.append(a[i])
    else:
        tosort.append(a[i])
    i += 1
tosort.sort()
answer = []
i = 0
j = 0
k = 0
while i < len(a):
    if i in b:
        answer.append(nottosort[j])
        j += 1
    else:
        answer.append(tosort[k])
        k += 1
    i += 1
print("The sequence you want is:",end = " ")
for i in answer:
    print(i,end=" ")
