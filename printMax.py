#Which is the max

def printMax():
    a=int(input('enter a number: '))
    b=int(input('enter another number: '))

    if(a>b):
        print(str(a) +' is greater than '+str(b))
    elif(a<b):
        print(str(a) +' is smaller than '+str(b))

    else:
        print(str(a) +' and '+str(b) +' are equal.')
        
        
printMax()
