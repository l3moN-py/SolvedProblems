from functools import cache
from itertools import product
import re

@cache
def isPrime(n):
    if n == 2:
        return True
    elif n % 2 == 0 or n == 1:
        return False
    for i in range(3,int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def foo():
    i = 56001
    while True:
        i += 2
        if sum(map(int, (str(i)))) % 3 == 0:
            pass
        elif isPrime(i):
            for adder in list(map(lambda t: int(''.join(list(map(str, t))))*10, product([0, 1], repeat=len(str(i))-1)))[1::]:
                c = 0
                mem = []
                for j in range(10):
                    num = list(str(i))
                    for indexes in list(map(lambda x: x.span()[0],list(re.finditer('1', str(adder))))):
                        ind = len(str(i))+indexes-len(str(adder))
                        if ind == 0 and j == 0:
                            break
                        else:
                            num[ind] = str(j)
                    else:
                        num = int(''.join(num))
                        # print(num)
                        if isPrime(num):
                            mem.append(num)
                            c += 1

                if c >= 8:
                    print(adder, i, mem)
                    return None

foo()

