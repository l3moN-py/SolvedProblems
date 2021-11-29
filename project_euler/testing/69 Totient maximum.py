import sympy
primes = list(sympy.primerange(0, 500_000))

rel_primes = {}

for num in range(2, 1_000_000):
    rel_prime = num
    for p in primes:
        if p > num:
            if rel_prime == 0:
                rel_primes.update({num: 0})
                break
            rel_primes.update({num: num/rel_prime})
            break
        elif num % p == 0:
            rel_prime -= (num-1)//p

print(sorted(rel_primes.items(), key=lambda x: x[1], reverse=True)[0])
