def check(old_num, new_num):
    new_num = str(new_num)
    for num in str(old_num):
        if num not in new_num:
            return False
    return True
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

prime_list = [prime for prime in range(10000,1000,-1) if isPrime(prime)]

for i in prime_list:
    if check(i, i-3330) and check(i, i-2*3330):
        if i in prime_list and i-3330 in prime_list and i-2*3330 in prime_list:
            print(str(i-2*3330) + str(i-3330) + str(i))
