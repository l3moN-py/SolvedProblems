def isPrime(n):
    if n == 2:
        return True
    elif n%2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True

c = 1
n = 1
while c != 10001:
    n += 2
    if isPrime(n):
        c += 1
    
print("Answer:", n)
