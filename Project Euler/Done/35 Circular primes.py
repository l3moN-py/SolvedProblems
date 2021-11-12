def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def circular(x):
    for i in range(len(str(x))):
        x = int(str(x)[1:] + str(x)[0])
        if not isPrime(x):
            return False
    return True
def do(l):
    for num in l:
        if circular(num):
            res.append(num)

res = [2]
prime_list = [a for a in range(1, 1000000, 2) if '2' not in str(a) and '4' not in str(a) and '6' not in str(a) and '8' not in str(a) and '0' not in str(a) and isPrime(a) and a != 1]

do(prime_list)

print('Answer:', len(res))
