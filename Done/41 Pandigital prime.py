from itertools import permutations as perm
from myLibrary import *
foo = 2
x = []
while foo < 11:
    for num in perm([n for n in range(1,foo)]):
        res = int(''.join([str(a) for a in num]))
        if isPrime(res):
            x.append(res)
    foo += 1
print('Answer:', x[-1])
