def addition(x,y,z):
    if x+y==z or z+y==x or z+x==y:
        return True
    return False 
def main():
    var1=int(input('please enter x:'))
    var2=int(input('please enter y:'))
    var3=int(input('please enter z:'))
    if addition(var1,var2,var3):
        print('Yes they mee the criteria')
    else:
        print('please enter correct number')

main()
