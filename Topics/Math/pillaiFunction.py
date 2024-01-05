from sympy.ntheory import totient, divisors
from random import sample

def pillai(n):
    return sum([n*totient(d)//d for d in divisors(n)])

for i in range(100):
    print(i, pillai(i))
