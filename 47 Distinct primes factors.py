def isPrime(n):
    if n%2 == 0:
        return False
    for i in range(3,int(n**0.5)+1, 2):
        if n%i==0:
            return False
    return True

def consecutive(n, x):
    for i in range(3, n+1, 2):
        if n%2 == 0 :
            n = n//2
            x.append(2)
            consecutive(n, x)
            break
        elif isPrime(n):
            x.append(n)
            break
        elif n%i == 0 and isPrime(i) and n%i == 0:
            n = n//i
            x.append(i)
            consecutive(n, x)
            break
    return len(set(x))

def test(i):
    for a in range(4):
        x = []
        if consecutive(i+a, x) != 4:
            return False
    return True

i = 1
while True:
    if test(i):
        print(i)
        break
    i += 1

#134043
#[Finished in 18.777s]

#134043
#[Finished in 10.097s]

#134043
#[Finished in 6.671s]
