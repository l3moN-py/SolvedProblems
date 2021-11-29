def isPrime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def check(num):
    for i in range(len(str(num)) - 1):
        if not isPrime(int(str(num)[:i+1])):
            return False
        if not isPrime(int(str(num)[i+1:])):
            return False
    return True
n = 8
t = 0
res = 0
while t != 11:
    if isPrime(n) and check(n):
        res += n
        t += 1
    n += 1
print('Answer:', res)
