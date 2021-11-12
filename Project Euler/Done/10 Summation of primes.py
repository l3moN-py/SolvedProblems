from myLibrary import *
print('Answer:', sum([2] + [a for a in range(3,2000000,2) if isPrime(a)]))
