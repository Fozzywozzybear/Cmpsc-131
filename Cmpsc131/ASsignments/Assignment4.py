#assignment 4
#Aaron fosmire
#ajf434
#collaborators Nate Malay joe

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
        if k[0] < k[1]:
            k.pop(0)
                
    u=len(k)
    for q in range (u+1):
        
        if k[0] < k[1]:
            
            return False
        if k[0]>k[1] and k[0]<k[1]:
            k.pop(0)
        if len(k)==2 and k[0]>k[1]:
            return True
        k.pop(0)
                    
    else:
        return True
                
            
        
    
def main():
    i = 0 
    n = input('please enter a number')
    k= [int(i) for i in n]
    if (upnumber(k)==True) or (downnumber(k)==True) or (updownnumber(k)==True):
        print ('Valid')
    else:
        print ('not valid')
    

main()

