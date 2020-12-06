def upnumber(k):
    if sorted(k)== k:
        return True
    else:
        return False
def downnumber(k) :
    if sorted(k,reverse=True)== k:
        return True
    else:
        return False
    
def updownnumber(k):
    t=len(k)
    for l in range (len(k)):
        if k[0] > k[1]:
            for h in range (k):
                print (k)
                k.pop(h)
                print (k)
    if t==len(k):
        print (k)
        return True
    u=len(k)
    for q in range (u+1):
        print (k)
        if k[q] < k[q+1]:
            print (k)
            return False
        if k[q]>k[q+1] and k[q]<k[q-1]:
            k.pop(0)
        if len(k)==2:
            return True
                
                    
    else:
        return True
                
            
        
    
def main():
    i = 0 
    n = input('please enter a number')
    k= [int(i) for i in n]
    print (upnumber(k))
    print (downnumber(k))
    print (updownnumber(k))
        

main()

