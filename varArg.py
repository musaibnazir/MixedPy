#Var Arg parameter::

def total(initial=5,*number,**keywords):
    count = initial
    for n in number:
        count+=n
        for key in keywords:
            count+=keywords[key]

        print( count)



total(10,1,2,3,vegetabls=50)        
        
