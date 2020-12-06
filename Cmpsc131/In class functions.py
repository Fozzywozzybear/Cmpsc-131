def findfibonacci(n):
    seq = [0,1]
    i = 2
    while i<=n:
        seq.append(0)
        seq[i] = seq[i-1] + seq[i-2]
        i +=1
    return seq[n]
        
    

    
    return fib[n-1]
def main():
    n=int(input('enter n:'))
    print(findfibonacci(n))


main()
    
