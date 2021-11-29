from math import factorial
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
i = 1
res = [1]
spiral = []
while i < 13:
    spiral.append([_ for _ in range(sum([_ for _ in range(i-1)]) * 8 + 2, sum([_ for _ in range(i)]) * 8 + 2)])
    i += 1
spiral[0] = [1]
#print(spiral[1][(1*2)*4- 1])

for proc in range(1,i-1):
    res += [spiral[proc][(proc*2)*1 - 1], spiral[proc][(proc*2)*2 - 1], spiral[proc][(proc*2)*3 - 1], spiral[proc][(proc*2)*4 - 1]]

print((len([a for a in res if isPrime(a) and a != 1]) / len(res)) * 100 )
