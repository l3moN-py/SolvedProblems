def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def foo(n):
    for num in prime:
        if num <= n:
            if (n-num) in multiply:
                return True
    return False
multiply = [2*(n**2) for n in range(0,10000)]
prime = [x for x in range(1,10000) if isPrime(x)]
p = 1

while foo(p):
    p += 2

print('Result: ', p)
