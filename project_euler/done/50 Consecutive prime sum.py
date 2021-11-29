def isPrime(n):
    if n == 2:
        return True
    elif n%2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True

t = 1000001
prime_list = [2]+[a for a in range(3, t, 2) if isPrime(a)]
c = 0
ans = 0


for i in range(len(prime_list)):
    if c > len(prime_list)-i:
        break
    for a in range(i, len(prime_list)+1, 2):
        l = prime_list[i:a+1]
        sl = sum(l)
        if sl > t:
            break
        elif isPrime(sl) and len(l) > c:
            c = len(l)
            ans = sl
print(ans)

#10001
#
#9521
#[Finished in 6.91s]
#
#9521
#[Finished in 5.193s]
#
#9521
#[Finished in 0.113s] xD
