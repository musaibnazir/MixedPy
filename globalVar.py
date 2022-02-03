#global var

x= 50
def func1():
    global x
    x=2
    print('local vaR is: '+str(x))
func1()
print('global vaR is: '+str(x))
