#fib 3

from functools import *

@lru_cache(maxsize=1000)
def fib(n):
    if type(n) != int:
        raise TypeError('n must be positive number!!')

    if n<1:
        raise ValueError('n must be positive!!')

    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n>2:
        return fib(n-1) + fib(n-2)
for n in range(1,50):
    print(fib(n+1)/fib(n))



fib(3)
