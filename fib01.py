#Fibonnaci Series::

def fib(n):
    if n == 1:
        return 1
    elif n ==2:
        return 1
    elif n>2:
        return fib(n-1) + fib(n-2)
for n in range(1,56):
    print(n,':',fib(n))



fib(n)    



