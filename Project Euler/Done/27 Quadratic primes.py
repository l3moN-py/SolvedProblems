#  n^2+an+b, where |a|<1000 and |b|≤1000

def isPrime(num):
    if [num//a for a in range(2,int(abs(num)**0.5) + 1) if num%a == 0] == []:
        return True
    return False
#print(isPrime(-999))
count = 0
result = 0
c = 0
for b in [i for i in range(1,1000,2) if isPrime(i) == True]:
    for a in range(-1000, 1000):
        c = 0
        for n in range(1000):
            if isPrime(n**2 + a*n + b) == False:
                break
            c += 1
        if c > count:
            count = c
            result = a*b

print('Answer:', result)
